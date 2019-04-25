from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import SI507project_db_query
import SI507project_db
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls



plotly.tools.set_credentials_file(username='jforan0127', api_key='WGk6w3RfTnsG16G7n8OL')
plotly.tools.set_config_file(world_readable=True, sharing='public')

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./SI507_final_databases.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
session = db.session

city_table = SI507project_db_query.city_query
system_table = SI507project_db_query.system_query



@app.route('/')
def homepage():
    return 'Welcome to Jen Forans SI507 project! <br><br><br><br><br><br> <a href="http://localhost:5000/systems_per_country">Click here to see Systems/Country. </a> <br><br> <a href="http://localhost:5000/ridership_by_stations">Click here to view Ridership vs # of Stations</a>. <br><br> <a href="http://localhost:5000/info">Click to Search a System.</a>'



@app.route('/systems_per_country')
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

    return render_template('stations_table.html',result=dict) + '<br><br><br><br><br><br> <a href="http://localhost:5000/">Click to Return Home. </a> <br><br> <a href="http://localhost:5000/ridership_by_stations">Click here to view Ridership vs # of Stations</a>. <br><br> <a href="http://localhost:5000/info">Click to Search a System.</a>'



@app.route('/ridership_by_stations')
def ridership_by_stations():
    ridership = []
    stations = []
    city = []
    for i in system_table:
        ridership.append(i.Ridership)
        stations.append(i.Number_of_stations)
        city_name = SI507project_db.session.query(SI507project_db.Cities).filter_by(id=i.City_id).first()
        city.append(city_name.City)

    for i in ridership:
        trace = go.Scatter(x = ridership, y = stations, text = city, mode = 'markers', textposition = 'top center')
        data = [trace]

        ## this would be used if to actually build the plotly graph.
        # return py.plot(data) + '<br><br><br><br><br><br> <a href="http://localhost:5000/">Click to Return Home. </a> <br><br> <a href="http://localhost:5000/systems_per_country">Click here to see Systems/Country. </a> <br><br> <a href="http://localhost:5000/info">Click to Search a System.</a>'

        ## this is the embedded graph.
        return tls.get_embed('https://plot.ly/~jforan0127/20') + '<br><br><br><br><br><br> <a href="http://localhost:5000/">Click to Return Home. </a> <br><br> <a href="http://localhost:5000/systems_per_country">Click here to see Systems/Country. </a> <br><br> <a href="http://localhost:5000/info">Click to Search a System.</a>'


@app.route('/info')
def info():
    return render_template('form1.html')

@app.route('/result',methods=["GET"])
def result_form1():
    if request.method == 'GET':
        system_result = request.args.get('system_input')

        if SI507project_db.session.query(SI507project_db.Systems).filter_by(Name=system_result).first():
            metro = SI507project_db.session.query(SI507project_db.Systems).filter_by(Name=system_result).first()
            name = metro.Name
            ridership = metro.Ridership
            stations = metro.Number_of_stations
            return "System Name: {} <br><br> Annual Ridership: {} million <br><br> Number of Stations: {}.".format(name, ridership,stations) + '<br><br><br><br><br><br> <a href="http://localhost:5000/">Click to Return Home. </a> <br><br> <a href="http://localhost:5000/systems_per_country"> Click here to view Ridership vs # of Stations </a>. <br><br> <a href="http://localhost:5000/systems_per_country">Click here to see Systems/Country. </a> <br><br> <a href="http://localhost:5000/info">Click to Search a System.</a>'


        else:
            return "This system does not exist :(" + '<br><br><br><br><br><br> <a href="http://localhost:5000/">Click to Return Home. </a> <br><br> <a href="http://localhost:5000/systems_per_country"> Click here to view Ridership vs # of Stations </a>. <br><br> <a href="http://localhost:5000/systems_per_country">Click here to see Systems/Country. </a> <br><br> <a href="http://localhost:5000/info">Click to Search a System.</a>'


if __name__ == '__main__':
    db.create_all()
    app.run()
