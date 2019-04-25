# World Metro Systems

Jen Foran

[Link to this repository](https://github.com/jforan/Final_Project_jlforan)

---


## Project Description

This project scrapes data from wikipedia's 'List of metro systems' page. It specifically collects all the information in the table saves and cleans it, then puts it into a CSV. After that, it is uploaded to a database where there are two tables: Cities and Systems. Cities holds city and country names, while Systems has system name, number of stations, and annual ridership. 

From there, a flask app is created with the following functionality:
* show the average number of stations for all stations, then the average number of stations per country. This will be a table.
* user will input the country of interest and the app will output the names of the stations in this country, along with their respective annual ridership.
* show a map in which with bubbles to indicate a city with a metro system.
* will have a plot indicating the relationship between ridership and stations via a scatterplot.
* allow users to add a new station with the appropriate other info: country, city, station name, number of stations, and annual ridership.


## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`
2. Second, you should run SI507project_tests.py to ensure that there is nothing wrong `python SI507project_tests.py`
3. Finally, run `python SI507project_flask.py runserver`.
4. If you click to the form entry (via 'Click to Search a System'), you can input 'Algiers Metro' (no quotes) to get information. To see what happens when the system does not exist, input 'Test System' (no quotes).


## How to use

PLEASE NOTE: this requires internet to be fully functional.

1. enter http://127.0.0.1:5000/ into the url. You will be greeted.
2. Select from one of the links at the bottom of the page. I suggest 'Click here to see Systems/Country.' This displays a list table of all of the countries in the database, and the number of systems associated to that country.
3. Select from one of the links at the bottom of the page. I suggest 'Click here to view Ridership vs # of Stations.' This shows a scatterplot of ridership vs. number of stations. PLEASE NOTE: the graph will not show if you are not connect to internet.
4. Select from one of the links at the bottom of the page. I suggest 'Click to Search a System.' Input 'Algiers Metro' into the field. It will return the Annual Ridership and number of stations associated to that system. 
5. At the bottom of the page, select 'Click to Search a System.' This time, enter 'Test System' (or your name or something that is not a metro system). It will return that this is not a metro system.



## Routes in this application
* `/` -> welcomes users
* `/stations_per_country` -> shows a list of all countries and number of stations per country
* `/ridership_by_stations` -> shows an embedded graph (code can be uncommented to make a new one) of ridership by number of stations. 
!! PLEASE NOTE: this requires you have internet to view the graph !!
* `/info` -> provides users with a form where they will input a station name which will prompt '/result'
* `/result` -> will show users the information associated with the station they entered into in '/info' (please note: it will tell you if the system does not exist and does not account for spelling errors.)


## How to run tests
* i need to work on these once i complete my tests


## In this repository:
* SI507project_scrape.py
* SI507project_db.py
* SI507project_db_query.py
* SI507project_flask.py
* SAMPLE_SI507_final_databases.sqlite
* SAMPLE_metro_export.csv
* db.py
* advanced_expiry_caching.py
* database_schema_diagram
* SAMPLE_cache_file.json
* README.md
* requirements.txt
* SI507project_tests.py
* [Folder] Pictures
  * home.png
  * systemsXcountry.png
  * ridershipXcountry.png
  * search.png
  * success_search.png
  * fail_search.png
* [Folder] templates
  * form1.html
  * stations_table.html
  

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module (plotly)
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
