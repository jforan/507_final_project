import SI507project_scrape
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
# from db import session, init_db, Base
import json
import csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import os
import sys


Base = declarative_base()
session = scoped_session(sessionmaker())

engine = create_engine('sqlite:///SI507_final_databases.sqlite', echo=False) # You might also have a config file, for example, that holds the string that is the db name. For now we'll just put it here.

Base.metadata.bind = engine
session.configure(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
    return engine



class Cities(Base):
    __tablename__ = 'cities'
    id = Column(Integer,primary_key = True, autoincrement = True)
    City = Column(String(250), nullable = False)
    Country = Column(String(250), nullable = False)

class Systems(Base):
    __tablename__ = 'systems'
    id = Column(Integer,primary_key = True, autoincrement = True)
    Name = Column(String(250))
    Number_of_stations = Column(Integer)
    Ridership = Column(Integer)
    City_id = Column(Integer, ForeignKey('cities.id'))
    cities = relationship("Cities")


init_db()

###################### uncomment if you would like to create tables
with open("metro_export.csv", 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data,None)

    list_of_citiescountries = []

    for i in csv_data:

        random_list = []
        if [i[0],i[1]] not in list_of_citiescountries:
            # print(i[0])
            random_list.append(i[0])
            # print(random_list)

            list_of_citiescountries.append([i[0],i[1]])

    # for i in list_of_citiescountries:
    #     print (i)
    for i in list_of_citiescountries:
        list = Cities(City = i[0], Country = i[1])
        session.add(list)
session.commit()


def getid(cityname):
    queryvar = session.query(Cities).filter(Cities.City == cityname).first()
    result = queryvar.id
    return result


with open("metro_export.csv", 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data,None)

    for i in csv_data:
        list_system_db = Systems(Name = i[3], Number_of_stations = i[2], Ridership = i[4], City_id = getid(i[0]))
        session.add(list_system_db)

session.commit()
