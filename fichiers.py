import requests
from bs4 import BeautifulSoup
from datetime import date

# Fonctions complémentaires pour apportées des données à insérer dans le fichier csv : 
# ------------------------------------------------
def get_page_content(year_month = "", end_point = "", ):
    url = f"https://www.spin-off.fr/{end_point}?date={year_month}" if year_month else f"https://www.spin-off.fr/{end_point}"

    # Request Content
    response = requests.get(url)
    content = response.content

    # Parse HTML
    return BeautifulSoup(content, features="html.parser")

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
# ------------------------------------------------


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
            
create_episode_csv(get_series())
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
            
print(read_episodes_csv())
# *************************************************