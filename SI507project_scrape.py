from bs4 import BeautifulSoup
import requests, json
from advanced_expiry_caching import Cache
import csv
import string
import unicodedata
import re

FILENAME = "cache_file.json"
program_cache = Cache(FILENAME)
url = 'https://en.wikipedia.org/wiki/List_of_metro_systems'

data = program_cache.get(url)
if not data:
    data = requests.get(url).text
    program_cache.set(url, data, expire_in_days=20)
soup = BeautifulSoup(data, "html.parser")

#print(soup.prettify())

table  = soup.find_all('table', class_="wikitable")
systems = table[0]
systems_list = systems.find_all('tr')[1:]
master = []

last_country = ['start']
last_city = ['start']

for s in systems_list:
    system = s.find_all("td")
    # print(len(system))

    if len(system) == 6:
        city = last_city[-1]
        country = last_country[-1]
        name = system[0].text.strip()
        stations = system[3].text.strip()

        try:
            ridership = system[5].text.strip()
        except:
            ridership = 'n/a'

        temp = [city,country, stations, name, ridership]
        master.append(temp)


    else:
        city = system[0].text.strip()
        country = system[1].text.strip()
        name = system[2].text.strip()
        stations = system[5].text.strip()

        try:
            ridership = system[7].text.strip()
        except:
            ridership = 'n/a'

        temp = [city, country, stations, name, ridership]
        master.append(temp)

        last_country.append(country)
        last_city.append(city)

# print(len(master))
# print(master)



#### cleaning data

metro_data = []

for i in master:

    list_of_items = []

    city_2 = re.sub(r'\([^)]*\)', '',i[0])
    city_22 = re.sub(r'\[[^()]*\]', '',city_2)

    country_2 = re.sub(r'\([^)]*\)', '',i[1])
    country_22 = re.sub(r'\[[^()]*\]', '',country_2)

    num_stations_2 = re.sub(r'\([^)]*\)', '',i[2])
    num_stations_22 = re.sub(r'\[[^()]*\]', '',num_stations_2)
    name_2 = i[3]
    ann_riders_2 = re.sub(r'\([^)]*\)', '',i[4])
    ann_riders_22 = re.sub(r'\[[^()]*\]', '',ann_riders_2)


    list_of_items.append(re.sub(r'\([^)]*\)', '',city_22))
    list_of_items.append(re.sub(r'\([^)]*\)', '',country_22))
    list_of_items.append(re.sub(r'\(.*\)', '',num_stations_22))
    list_of_items.append(re.sub(r'\[.*\]', '',name_2))
    list_of_items.append(re.sub(r'\([^)]*\)', '',ann_riders_22))

    # print(re.sub(r'\([^)]*\)', '',ann_riders))
    # print(num_stations2)

    metro_data.append(list_of_items)

# print(metro_data)
#
#
# # export to csv
#
header = ['City', 'Country', 'Number of Stations', 'Name', 'Ridership']

with open('metro_export.csv', 'w',encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in metro_data:
        writer.writerow(i)
