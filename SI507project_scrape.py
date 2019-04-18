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
#print(systems_list[-5:])
# print(len(systems_list[0].find_all("td")))
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
