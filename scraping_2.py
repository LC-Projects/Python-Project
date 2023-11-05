import time
from utils import *


# *************************************************
# Scraping [2/2] 
# 4️⃣ Sur les pages individuelles des épisodes (dont l’url à été récupérée lors de la première question), récupérer la durée de l’épisode. Les requêtes peuvent être un peu longue donc vous pouvez ne le faire que pour une seule chaîne comme Apple TV. Veiller à ne pas perdre les données pour pouvoir les insérer dans SQL. Pensez à utiliser un time.sleep entre les requêtes.
def get_episodes_duration():
    cur = sqlite_connection()
    
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
