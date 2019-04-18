import SI507project
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
# from db import session, init_db, Base
import json
import csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


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
    Name = Column(String(250),ForeignKey('cities.id'))
    Number_of_stations = Column(Integer)
    Ridership = Column(Integer)
    cities = relationship("City")


init_db()

## load in datasets (2)


with open("metro_export.csv", 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data,None)

    for i in csv_data:
        print(i[0])
        # for e in i[4]:
        #     updated = e[:-1]
        #     f_updated = float(updated)
        list_countries = Cities(City = i[0], Country = i[1])
        session.add(list_countries)

session.commit()


def getid(cityname):
    queryvar = session.query(City).filter(City.City == cityname).first()
    result = queryvar.id
    return result


with open("metro_export.csv", 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data,None)

    for i in csv_data:
        print(i[0])
        # for e in i[4]:
        #     updated = e[:-1]
        #     f_updated = float(updated)
        list_system_db = Systems(Name = i[3], Number_of_stations = i[2], Ridership = i[4])
        session.add(list_system_db)

session.commit()
