import requests
from bs4 import BeautifulSoup
from datetime import date


# 1️⃣ Récupérer les données relatives à la diffusion d’épisodes pour le mois en cours disponibles sur cette page :  
def get_series():
    url = "https://www.spin-off.fr/calendrier_des_series.html"

    # Request Content
    response = requests.get(url)
    content = response.content

    # Parse HTML
    page = BeautifulSoup(content, 'html')


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

    # print(list_of_series)
    # print("Le nom de la série (", len(list_of_series_name), ") : ", list_of_series_name)
    # print("Le numéro de l’épisode (", len(list_of_series_episode), ") : ", list_of_series_episode)
    # print("Le numéro de la saison (", len(list_of_series_season), ") : ", list_of_series_season)
    # print("La date de diffusion de l’épisode (", len(list_of_series_origin), ") : ", list_of_series_origin)
    # print("Le pays d’origine (", len(list_of_series_channel), ") : ", list_of_series_channel)
    # print("La chaîne qui diffuse la série (", len(list_of_series_date), ") : ", list_of_series_date)
    # print("L’url relative de la page de l’épisode sur le site spin-off  (", len(list_of_series_url), ") : ", list_of_series_url)

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




# 3️⃣ Écrire une fonction ou une classe qui permet de lire le fichier episodes.csv sans utiliser de librairie. Cette fonction ou classe devra renvoyer une liste de tuples avec les bons types : 
def read_episode_csv():       
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
            
# print(read_episode_csv())