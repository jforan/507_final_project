from SI507project_db import Base, Systems, Cities
from db import session, init_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import SI507project_db


engine = create_engine('sqlite:///SI507_final_databases.sqlite')
SI507project_db.Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# print(session.query(SI507project_db.Systems).all())



city_query = session.query(Cities).all()
system_query = session.query(Systems).all()
# print(example.City)
# print(example2.Name)
