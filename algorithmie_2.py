from utils import *

# # *************************************************
# Algorithmie [2/2]
# 5️⃣ Quelle est la chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs sur le mois de novembre ? (écrire une fonction qui permet de répondre à cet question)
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

print(most_diffused_channel("2023-11"))
# *************************************************
