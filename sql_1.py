import sqlite3
from datetime import date

# Fonctions complémentaires pour apportées des données à insérer dans le fichier csv : 
# ------------------------------------------------
def read_episodes_csv():       
    with open('data/files/episodes.csv', 'r') as file:
        content = file.read()
        typed_content = []
        for serie in content.split("\n")[1:]:
            serie_elements = serie.split(",")            
            
            # Épisodes
            if serie_elements[1]:
                if serie_elements[1].isalpha():
                    serie_elements[1] = -1
                else:
                    serie_elements[1] = (int(serie_elements[1]))
                    
            # Saisons  
            if serie_elements[2]:
                if serie_elements[2].isalpha():
                    serie_elements[2] = 0
                else:
                    serie_elements[2] = (int(serie_elements[2]))
                    
            # Date de diffusion  
            if serie_elements[3]:
                serie_date = serie_elements[3].split("-")
                year = int(serie_date[2])
                month = int(serie_date[1])
                day = int(serie_date[0])
                serie_elements[3] = date(year, month, day)
                    
            typed_content.append(tuple(serie_row for serie_row in serie_elements))
        return typed_content
# ------------------------------------------------


# *************************************************
# SQL [1/2]
# 2️⃣ Insérer les données de la question Scraping [1/2] dans base de données sqlite appelée database.db dans le dossier data/databases. La table devra s’appeler episode .
# Veillez à utiliser les types adéquats (la date peut toutefois être stockée en tant que chaîne de caractères avec un typeTEXT).
def episodes_to_database():
    # Connexion à la base de données (si elle n'existe pas, elle sera créée)
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

    # Décommenter ci-dessous pour tester la lecture
    cur.execute("SELECT * FROM episode")
    resultats = cur.fetchall()
    for row in resultats:
        print(row)

episodes_to_database()
# *************************************************
