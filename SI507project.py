import SI507project_scrape
import csv
import string
import unicodedata
from bs4 import BeautifulSoup
import re

table = SI507project_scrape.soup.find('table')

headers = [table.find_all('tr')[0]]
metro_data = []

# print(SI507project_scrape.systems.find_all('tr')[0])

# re.sub(r'\(.*\)', '', 'stuff(remove(me))')

for i in SI507project_scrape.master:
    list_of_items = []

    city = i[0]
    country = i[1]
    num_stations = re.sub(r'\([^)]*\)', '',i[5])
    num_stations2 = re.sub(r'\[[^()]*\]', '',num_stations)
    name = i[2]
    ann_riders = re.sub(r'\([^)]*\)', '',i[6])
    ann_riders2 = re.sub(r'\[[^()]*\]', '',ann_riders)


    list_of_items.append(re.sub(r'\([^)]*\)', '',city))
    list_of_items.append(re.sub(r'\([^)]*\)', '',country))
    list_of_items.append(re.sub(r'\(.*\)', '',num_stations2))
    list_of_items.append(re.sub(r'\[.*\]', '',name))
    list_of_items.append(re.sub(r'\([^)]*\)', '',ann_riders2))

    # print(re.sub(r'\([^)]*\)', '',ann_riders))
    # print(num_stations2)

    metro_data.append(list_of_items)

# print(metro_data)


# export to csv

header = ['City', 'Country', 'Number of Stations', 'Name', 'Ridership']

with open('metro_export.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in metro_data:
        writer.writerow(i)
