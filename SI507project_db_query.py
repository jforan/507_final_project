from SI507project_db import Base, Systems, Cities
from db import session, init_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import SI507project_db
import SI507project_tools
# from tabulate import tabulate
from prettytable import PrettyTable


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




### put into table ###
# dict = {}
# for i in system_query:
#     # print(i.City_id)
#     city_name = session.query(Cities).filter_by(id=i.City_id).first()
#
#     if city_name.Country not in dict:
#         dict[city_name.Country] = 1
#     else:
#         dict[city_name.Country] += 1
#
# table = PrettyTable(['Country', 'Number of Stations'])
# for i in dict:
#     table.add_row([i, dict[i]])
#
# # print(table)
#










# all_movies = []
# for m in example2:
#     director = session.query(Cities).filter_by(id=m.City_id).first()
#     all_movies.append((m.Name,director.Country))
#
# print(all_movies)

#
# engine = init_db()
# # Again -- all the boilerplate that has to go together to rely on the session for doing easy insertions/queries in Python. We need access to an engine now, so we'll capture the return val from init_db.
#
#
# # Now let's write some code to do some queries
# # Wouldn't always just do this in a script -- might do it... in a separate application and simply write code to create and populate the db, for example!
# # But let's try to see how it will work, because we'll rely on this type of structure for more stuff later.
#
#
# # If only use SQL select statement without ORM...
# connection = engine.connect()
# result = connection.execute("select * from cities")
# for row in result:
#     print(row)
# connection.close()
#
#
# # Almost there but not quite
# session.query(Cities) # Doesn't get us anywhere that useful if we run this line -- it's just a query object this evaluates to! No data we can see, not stored anywhere in the *program*...
#
# # Actually query for all the universities in the database
# all_unis = session.query(cities).all() # That last method *gets* -- and returns -- something that acts a lot like a list...
# print(all_unis) # Let's see it
# #
# # # Just the first university in the database
# first_uni = session.query(Cities).first()
# print(first_uni) # Let's see it
#
# # Wait... this is no good, they don't look like anything!!!
#
# # Can we print out any data values?
#
# # for u in all_unis:
# #     print(u.name)
# #     print("^ is at", u.location)
