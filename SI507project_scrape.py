from bs4 import BeautifulSoup
import requests, json
from advanced_expiry_caching import Cache

FILENAME = "cache_file.json"

program_cache = Cache(FILENAME)

url = 'https://en.wikipedia.org/wiki/List_of_metro_systems'

data = program_cache.get(url)
if not data:
    data = requests.get(url).text
    #print(data) # to prove it - this will print out a lot

    program_cache.set(url, data, expire_in_days=20)

soup = BeautifulSoup(data, "html.parser")

#print(soup.prettify())

table  = soup.find_all('table', class_="wikitable")
systems = table[0]
systems_list = systems.find_all('tr')[1:]
# print(len(systems_list[0].find_all("td")))
master = []

for s in systems_list:
    system = s.find_all("td")
    try:
        ridership = system[7].text.strip()
    except:
        ridership = 'n/a'
    temp = [
    system[0].text.strip(),
    system[1].text.strip(),
    system[2].text.strip(),
    system[3].text.strip(),
    system[4].text.strip(),
    system[5].text.strip(),
    ridership
    ]
    master.append(temp)

# print(len(master))
# print(master)
