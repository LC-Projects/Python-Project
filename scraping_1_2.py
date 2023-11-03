import requests
from bs4 import BeautifulSoup

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
print("Le nom de la série (", len(list_of_series_name), ") : ", list_of_series_name)
print("Le numéro de l’épisode (", len(list_of_series_episode), ") : ", list_of_series_episode)
print("Le numéro de la saison (", len(list_of_series_season), ") : ", list_of_series_season)
print("La date de diffusion de l’épisode (", len(list_of_series_origin), ") : ", list_of_series_origin)
print("Le pays d’origine (", len(list_of_series_channel), ") : ", list_of_series_channel)
print("La chaîne qui diffuse la série (", len(list_of_series_date), ") : ", list_of_series_date)
print("L’url relative de la page de l’épisode sur le site spin-off  (", len(list_of_series_url), ") : ", list_of_series_url)