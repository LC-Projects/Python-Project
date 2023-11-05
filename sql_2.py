import sqlite3
import time

# Fonctions complémentaires pour apportées des données à insérer dans le fichier csv : 
# ------------------------------------------------
def get_episodes_duration():
    # Connexion à la base de données (si elle n'existe pas, elle sera créée)
    conn = sqlite3.connect('data/databases/database.db')

    # Création d'un curseur pour exécuter des commandes SQL
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM episode WHERE chaine_diffusion LIKE 'Apple TV+'")
    series = cur.fetchall()

    durations = []
    for serie in series:    
        page = get_page_content(False, serie[7])
        duration = page.find('div', class_='episode_infos_episode_format').text.replace("minutes", "").strip()
        
        if duration != "":
            durations.append([serie[0], int(duration)])
        else:
            durations.append([serie[0], 0])
        time.sleep(1)

    return durations
# ------------------------------------------------


# *************************************************
# SQL [2/2]
# 4️⃣ Stocker les données de durée d’épisode (en minutes) dans une nouvelles table duration qui contiendra une Foreign Key pointant sur l’épisode en question dans la table episode 
def save_duration_to_database(data):
    # Connexion à la base de données (si elle n'existe pas, elle sera créée)
    conn = sqlite3.connect('data/databases/database.db')

    # Création d'un curseur pour exécuter des commandes SQL
    cur = conn.cursor()

    # Create Table Schema
    cur.execute("""
        CREATE TABLE IF NOT EXISTS duration (
            id   INTEGER PRIMARY KEY,
            duration INTEGER,
            duration_id INTEGER,
            FOREIGN KEY (duration_id)
                REFERENCES episode (id) 
        )
    """)
    conn.commit()


    # Insert Data
    cur.executemany("""INSERT INTO duration 
                    (
                        duration_id,
                        duration
                    ) VALUES (?,?)""",
                    data)
    conn.commit()
    
save_duration_to_database(get_episodes_duration())
# *************************************************
