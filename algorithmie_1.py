import requests
from bs4 import BeautifulSoup

# Fonctions complémentaires pour apportées des données à insérer dans le fichier csv : 
# ------------------------------------------------
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
# ------------------------------------------------

    
# *************************************************
# Algorithmie [1/2]
# 3️⃣ Calculer le nombre d’épisodes diffusés par chaque chaîne de télévision (présente dans les données) en Octobre.
# property_name → "nom_serie", "numero_de_lepisode", "numero_de_la_saison", "date_de_diffusion_de_lepisode", "pays_d_origine", "chaine_de_diffusion", "url_relative_de_lepisode"
def count_episodes_by_property(year_month, property_name):
    properties = get_series(year_month)[property_name]
    return count(properties)

print(count_episodes_by_property("2023-10", "chaine_de_diffusion"))
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
    return count(words)

print(most_used_word_in_show_title())
# *************************************************
