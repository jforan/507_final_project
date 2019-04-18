# -*- coding: utf-8 -*-
import SI507project_scrape
import csv
import string
import unicodedata
from bs4 import BeautifulSoup
import re


metro_data = []


for i in SI507project_scrape.master:

    list_of_items = []

    city_2 = i[0]
    country_2 = i[1]
    num_stations_2 = re.sub(r'\([^)]*\)', '',i[2])
    num_stations_22 = re.sub(r'\[[^()]*\]', '',num_stations_2)
    name_2 = i[3]
    ann_riders_2 = re.sub(r'\([^)]*\)', '',i[4])
    ann_riders_22 = re.sub(r'\[[^()]*\]', '',ann_riders_2)


    list_of_items.append(re.sub(r'\([^)]*\)', '',city_2))
    list_of_items.append(re.sub(r'\([^)]*\)', '',country_2))
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
