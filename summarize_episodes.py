# Pour le mois de novembre
# python3 summarize_episodes.py --month 11


import argparse
from main import *
import datetime

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--month", help="Month (1-12)")

args = argParser.parse_args()
year = datetime.datetime.now().year
months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
if args.month.isnumeric():
    month = int(args.month)
    if month in range(1,13):
        page_data = get_series(f"{year}-{month}")
        
        print("***********************\n")
        print((f"Pour le mois de {months[month - 1]} \n").upper())
        print(" ".join(
            [
                str(len(page_data["nom_serie"])),
                "episodes seront diffusés pendant le mois de",
                months[month - 1] + "."
            ]
        ) + "\n")
        
        countries = count(page_data["pays_d_origine"])
        country_name = list(countries)[0]
        country_value = list(countries.values())[0]
        print(" ".join(
            [
                "C'est",
                country_name,
                "qui diffusera le plus d'épisodes avec",
                str(country_value),
                "épisodes."
            ]
        ))
        print("\n***********************")
        
    else:
        print("Your number should be between 1 and 12")
else:
    print("WTF ??")