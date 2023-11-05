from utils import *
from scraping_1 import *




# *************************************************
# Algorithmie [1/2]
# 3️⃣ Calculer le nombre d’épisodes diffusés par chaque chaîne de télévision (présente dans les données) en Octobre.
# property_name → "nom_serie", "numero_de_lepisode", "numero_de_la_saison", "date_de_diffusion_de_lepisode", "pays_d_origine", "chaine_de_diffusion", "url_relative_de_lepisode"
def count_episodes_by_property(year_month, property_name):
    properties = get_series(year_month)[property_name]
    return count(properties)

print(count_episodes_by_property("2023-11", "chaine_de_diffusion"))
# *************************************************



# *************************************************
# 3️⃣ Faire de même pour les pays (pensez à mutualiser votre code !)
print(count_episodes_by_property("2023-10", "pays_d_origine"))
# *************************************************



# *************************************************
# 3️⃣ Quels mots reviennent le plus souvent dans les noms des séries ? (attention à ne compter qu’une seule fois chaque série, et pas une fois chaque épisode)
# Les indiquer dans le fichier README.md
def most_used_word_in_show_title(year_month):
    shows_title = [key for key in count_episodes_by_property(year_month, "nom_serie")]
    words = []
    for show_title in shows_title:
        for word in show_title.split(" "):
            words.append(word.upper())
    return count(words)

print(most_used_word_in_show_title("2023-11"))
# *************************************************