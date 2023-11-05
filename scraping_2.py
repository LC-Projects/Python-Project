import requests
import sqlite3
import time
from bs4 import BeautifulSoup

# Fonctions complémentaires pour apportées des données à insérer dans le fichier csv : 
# ------------------------------------------------
def get_page_content(year_month = "", end_point = "", ):
    url = f"https://www.spin-off.fr/{end_point}?date={year_month}" if year_month else f"https://www.spin-off.fr/{end_point}"

    # Request Content
    response = requests.get(url)
    content = response.content

    # Parse HTML
    return BeautifulSoup(content, features="html.parser")
# ------------------------------------------------


# *************************************************
# Scraping [2/2] 
# 4️⃣ Sur les pages individuelles des épisodes (dont l’url à été récupérée lors de la première question), récupérer la durée de l’épisode. Les requêtes peuvent être un peu longue donc vous pouvez ne le faire que pour une seule chaîne comme Apple TV. Veiller à ne pas perdre les données pour pouvoir les insérer dans SQL. Pensez à utiliser un time.sleep entre les requêtes.
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
        
print(get_episodes_duration())
# *************************************************
