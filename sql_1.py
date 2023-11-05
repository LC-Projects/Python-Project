from datetime import date
from utils import *
from fichiers import *




# *************************************************
# SQL [1/2]
# 2️⃣ Insérer les données de la question Scraping [1/2] dans base de données sqlite appelée database.db dans le dossier data/databases. La table devra s’appeler episode .
# Veillez à utiliser les types adéquats (la date peut toutefois être stockée en tant que chaîne de caractères avec un typeTEXT).
def episodes_to_database():    # Connexion à la base de données (si elle n'existe pas, elle sera créée)
    conn = sqlite3.connect('data/databases/database.db')

    # Création d'un curseur pour exécuter des commandes SQL
    cur = conn.cursor()

    # Définir le schéma de la table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS episode (
            id INTEGER PRIMARY KEY,
            nom_serie TEXT,
            numero_episode INTEGER,
            numero_saison INTEGER,
            date_diffusion DATE,
            pays_origine TEXT,
            chaine_diffusion TEXT,
            url_episode TEXT
        )
    ''')
    conn.commit()


    # Insérer les données
    cur.executemany("""INSERT INTO episode 
                    (
                        nom_serie,
                        numero_episode,
                        numero_saison,
                        date_diffusion,
                        pays_origine,
                        chaine_diffusion,
                        url_episode
                    ) VALUES (?,?,?,?,?,?,?)""",
                    read_episodes_csv())
    conn.commit()

    print("Add successfully to database")

    # Décommenter ci-dessous pour tester la lecture
    # cur.execute("SELECT * FROM episode")
    # resultats = cur.fetchall()
    # for row in resultats:
    #     print(row)

episodes_to_database()
# *************************************************
