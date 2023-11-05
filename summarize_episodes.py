import argparse
import datetime
from main import *

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--month", help="Month (1-12)")

args = argParser.parse_args()
year = datetime.datetime.now().year
months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
if args.month.isnumeric():
    month = int(args.month)
    if month in range(1,13):
        current = f"{year}-{month}"
        page_data = get_series(current)
        
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
        ) + "\n")
        
        
        channels = count(page_data["chaine_de_diffusion"])
        channel_name = list(channels)[0]
        channel_value = list(channels.values())[0]
        print(" ".join(
            [
                "C'est",
                channel_name,
                "qui diffusera le plus d'episodes avec",
                str(channel_value),
                "épisodes."
            ]
        ) + "\n")
   

        channels_in_a_row = most_diffused_channel(current)
        channel_in_a_row_name = list(channels_in_a_row)[0]
        channel_in_a_row_value = list(channels_in_a_row.values())[0]
        print(" ".join(
            [
                "C'est",
                channel_in_a_row_name,
                "qui diffusera des épisodes pendant le plus grand nombre de jours consécutifs avec",
                str(channel_in_a_row_value),
                "de jours consécutifs."
            ]
        ))
        print("\n***********************")
        
    else:
        print("Your number should be between 1 and 12")
else:
    print("WTF ??")