from datetime import date
from scraping_1 import *
from utils import *




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
            
create_episode_csv(get_series("2023-11"))
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