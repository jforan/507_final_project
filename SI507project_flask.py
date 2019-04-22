from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import SI507project_db_query
import SI507project_db
# from prettytable import PrettyTable
import flask_table
# import plotly.plotly as py
# import plotly.graph_objs as go


app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./movies.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
session = db.session

city_table = SI507project_db_query.city_query
system_table = SI507project_db_query.system_query


## Main route
@app.route('/')
def homepage():
    # return "Welcome to Jen Foran's SI507 project!"
    return 'Welcome to Jen Forans SI507 project!. <br><br> <a href="http://localhost:5000/stations_per_country">Click here to see Stations/Country.'
    # </a> <br><br> <a href="http://localhost:5000/all_vehicles">Click here to see all vehicles</a>.'


@app.route('/stations_per_country')
def stations():
    dict = {}
    for i in system_table:
        # print(i.City_id)
        city_name = SI507project_db.session.query(SI507project_db.Cities).filter_by(id=i.City_id).first()

        if city_name.Country not in dict:
            dict[city_name.Country] = 1
        else:
            dict[city_name.Country] += 1


    class Item(object):
        def __init__(self, name, description):
            self.name = name
            self.description = description

    return render_template('stations_table.html',result=dict)



# @app.route('/ridership_by_stations')
# def ridership_by_stations():


## Flask-Forms-DB-example-master
# @app.route('/new')
# def new():

# @app.route('/result',methods=["GET"])
# def result_form1():
#     if request.method == "GET":
#         print(request.args) # Check out your Terminal window where you're running this... to see
#         if len(request.args) > 0:
#             for k in request.args:
#                 poss_type = request.args.get(k,"None") # in two steps for clarity
#                 veh = Vehicle.query.filter_by(type=poss_type).first()
#                 if not veh:
#                     veh = Vehicle(type=request.args.get(k,"None"),number_owned=0) # start
#                     session.add(veh)
#                     session.commit()
#                 veh.number_owned += 1
#                 session.add(veh)
#                 session.commit()
#             return "Vehicles (or lack thereof) successfully noted. <br><br> <a href='http://localhost:5000/'>Go to the main page</a>"








#     movies = Movie.query.all()
#     num_movies = len(movies)
#     return render_template('movie_count.html', num_movies=num_movies)
#
# @app.route('/movie/new/<title>/<mpaarating>/<director>')
# def new_movie(title, mpaarating, director):
#     if Movie.query.filter_by(title=title).first():
#         return "That movie already exists, go back to the homepage!"
#     else:
#         director = get_or_create_director(director)
#         movie = Movie(title=title, director_id=director.id,mpaa_rating=mpaarating)
#         session.add(movie)
#         session.commit()
#         return "New movie: {} by {}.".format(movie.title, director.name)
#
#
# @app.route('/all_movies')
# def see_all():
#     all_movies = []
#     movies = Movie.query.all()
#     for m in movies:
#         director = Director.query.filter_by(id=m.director_id).first()
#         all_movies.append((m.title,director.name, m.mpaa_rating))
#     return render_template('all_movies.html',all_movies=all_movies)
#
#
if __name__ == '__main__':
    db.create_all()
    app.run()
