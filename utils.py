import requests
import sqlite3
from bs4 import BeautifulSoup


def get_page_content(year_month = "", end_point = "", ):
    url = f"https://www.spin-off.fr/{end_point}?date={year_month}" if year_month else f"https://www.spin-off.fr/{end_point}"

    # Request Content
    response = requests.get(url)
    content = response.content

    # Parse HTML
    return BeautifulSoup(content, features="html.parser")


def sqlite_connection():
    # Connexion à la base de données (si elle n'existe pas, elle sera créée)
    conn = sqlite3.connect('data/databases/database.db')

    # Création d'un curseur pour exécuter des commandes SQL
    return conn.cursor()


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