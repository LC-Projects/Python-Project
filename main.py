import requests
import sqlite3
import time
from bs4 import BeautifulSoup
from datetime import date
import sys


# *************************************************
# REFACTO FUNCTIONS
def count(property_name, reverse = True, sort = True):
    counts = {}
    for element in property_name:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    if sort == True:
        return dict(sorted(counts.items(), key=lambda item: item[1], reverse=reverse))
    else:
        return counts
    
def get_page_content(year_month = "", end_point = "", ):
    url = f"https://www.spin-off.fr/{end_point}?date={year_month}" if year_month else f"https://www.spin-off.fr/{end_point}"

    # Request Content
    response = requests.get(url)
    content = response.content

    # Parse HTML
    return BeautifulSoup(content, features="html.parser")




# *************************************************
# 1️⃣ Récupérer les données relatives à la diffusion d’épisodes pour le mois en cours disponibles sur cette page :  
def get_series(year_month = ""):
    # Parse HTML
    page = get_page_content(year_month, "calendrier_des_series.html")

    list_of_series = [serie_name for serie_name in page.find_all('span',class_=['calendrier_episodes'])]

    # Le nom de la série
    list_of_series_name = [serie_name.find_all("a")[0].text for serie_name in list_of_series]

    # Le numéro de l’épisode
    list_of_series_episode = [serie_episode.find_all("a")[1].text.split(".")[1] for serie_episode in list_of_series]

    # Le numéro de la saison
    list_of_series_season = [serie_season.find_all("a")[1].text.split(".")[0] for serie_season in list_of_series]

    # La date de diffusion de l’épisode
    list_of_series_date = [serie_date.find_previous_sibling("div").get("id").strip("jour_") for serie_date in list_of_series]

    # Le pays d’origine
    list_of_series_origin = [serie_origin.find_previous_sibling().find_previous_sibling().get("alt") for serie_origin in list_of_series]

    # La chaîne qui diffuse la série
    list_of_series_channel = [serie_channel.find_previous_sibling().get("alt") for serie_channel in list_of_series]

    # L’url relative de la page de l’épisode sur le site spin-off 
    # (par exemple : episode01-408094-01102023-saison14-Bob-s-Burgers.html)
    list_of_series_url = [serie_url.find_all("a")[1].get('href') for serie_url in list_of_series]

    return {
        "nom_serie": list_of_series_name, 
        "numero_de_lepisode": list_of_series_episode, 
        "numero_de_la_saison": list_of_series_season, 
        "date_de_diffusion_de_lepisode": list_of_series_date, 
        "pays_d_origine": list_of_series_origin, 
        "chaine_de_diffusion": list_of_series_channel, 
        "url_relative_de_lepisode": list_of_series_url
    }
    
# print(get_series())
# *************************************************




# *************************************************
# 1️⃣ Enregistrez ces données dans un fichier episodes.csv dans le dossier data/files (vous pouvez utiliser une librairie) :
def create_episode_csv(data):
    header = [key for key in data]    
    data_values = [data[key] for key in data]
    
    rows = []
    # On parcourt la liste (sachant que chaque liste a la même longueur)
    for column in range(len(data_values[0])):
        row = []
        for index in range(len(data_values)):
            row.append(data_values[index][column])
        rows.append(row)
        
    with open('data/files/episodes.csv', 'w+') as file:
        file.write(",".join(header))
        for row in rows:
            file.write("\n" + ",".join(row))
            
# create_episode_csv(get_series())
# *************************************************




# *************************************************
# 3️⃣ Écrire une fonction ou une classe qui permet de lire le fichier episodes.csv sans utiliser de librairie. Cette fonction ou classe devra renvoyer une liste de tuples avec les bons types : 
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
            
# print(read_episodes_csv())
# *************************************************




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

# episodes_to_database()
# *************************************************




# *************************************************
# Algorithmie [1/2]
# 3️⃣ Calculer le nombre d’épisodes diffusés par chaque chaîne de télévision (présente dans les données) en Octobre.
# property_name → "nom_serie", "numero_de_lepisode", "numero_de_la_saison", "date_de_diffusion_de_lepisode", "pays_d_origine", "chaine_de_diffusion", "url_relative_de_lepisode"
def count_episodes_by_property(year_month, property_name):
    properties = get_series(year_month)[property_name]
    return count(properties)

# print(count_episodes_by_property("2023-10", "chaine_de_diffusion"))
# *************************************************




# *************************************************
# Vous pouvez faire directement des requêtes SQL, ou rapatrier les données depuis une table (ou un fichier dans lequel vous les auriez stocker) et faire les calculs avec Python. 
# Indiquer dans le fichier README.md le nom des trois chaînes qui ont diffusé le plus d’épisodes. 
# *************************************************




# *************************************************
# 3️⃣ Faire de même pour les pays (pensez à mutualiser votre code !)
# print(count_episodes_by_property("2023-10", "pays_d_origine"))
# *************************************************




# *************************************************
# 3️⃣ Quels mots reviennent le plus souvent dans les noms des séries ? (attention à ne compter qu’une seule fois chaque série, et pas une fois chaque épisode)
# Les indiquer dans le fichier README.md
def most_used_word_in_show_title():
    shows_title = [key for key in count_episodes_by_property("2023-10", "nom_serie")]
    words = []
    for show_title in shows_title:
        for word in show_title.split(" "):
            words.append(word.upper())
    
    # return (next(iter(count(words))))
    return count(words)

# print(most_used_word_in_show_title())
# *************************************************




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
        
# print(get_episodes_duration())
# *************************************************




# *************************************************
# SQL [2/2]
# 4️⃣ Stocker les données de durée d’épisode (en minutes) dans une nouvelles table duration qui contiendra une Foreign Key pointant sur l’épisode en question dans la table episode 
def save_duration_to_database():
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
                    get_episodes_duration())
    conn.commit()
    
# save_duration_to_database()
# *************************************************




# *************************************************
# Algorithmie [2/2]
# 5️⃣ Quelle est la chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs sur le mois d’Octobre ? (écrire une fonction qui permet de répondre à cet question)
def most_diffused_channel(year_month):
    page = get_page_content(year_month, "calendrier_des_series.html")

    list_of_channels_by_day = [[key for key in count([channel.find_previous_sibling("img").get("alt") for channel in serie_name.find_all("span", class_="calendrier_episodes")], False, False)] for serie_name in page.find_all('td',class_=['td_jour']) if serie_name.find("div", class_="div_jour")]

    all_channels_of_the_month = []
    for list_of_channels_of_the_day in list_of_channels_by_day:
        for channel_of_the_day in list_of_channels_of_the_day:
            all_channels_of_the_month.append(channel_of_the_day)
            
    all_channels_keyname = [key for key in count(all_channels_of_the_month, False, False)]
            
    counter_final = {}
    counter_tmp = {}
    
    # Initiate all channels at 0
    for channel in all_channels_keyname:
        counter_final[channel] = 0
        counter_tmp[channel] = 0
        
    # Begin counter
    for list_of_channels_of_the_day in list_of_channels_by_day:
        counter = {channel_of_the_day: 0 for channel_of_the_day in list_of_channels_of_the_day}
        for channel in all_channels_keyname:        
            if channel in list_of_channels_of_the_day:
                counter_tmp[channel] += 1
                if counter_tmp[channel] > counter_final[channel]:
                    counter_final[channel] = counter_tmp[channel]
            else:
                counter_tmp[channel] = 0
     
    # print(dict(sorted(counter_tmp.items(), key=lambda item: item[1], reverse=True)))
    return dict(sorted(counter_final.items(), key=lambda item: item[1], reverse=True))

# print(most_diffused_channel("2023-10"))
# *************************************************
