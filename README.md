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
2. Second, you should run SI507project_tests.py to ensure that there is nothing wrong
3. Finally, run `python SI507project_flask.py runserver`

## How to use

* i need more information on what is meant by this

## Routes in this application
- `/home` -> welcomes users
- `/station/countryaverage` -> shows users average number of stations/country in a table
- `/systems` -> form where users type country and the output is all systems from that country
- `/system/map` -> map with all systems tagged
- `/station/ridership` -> plot indicating the relationship between ridership and stations via a scatterplot.
- `/system/new` -> form where users input all the info for a new system

## How to run tests
* i need to work on these once i complete my tests

## In this repository:
- SI507project_scrape.py
- SI507project.py
- SI507project_tools.py
- SI507_Final_Project_Proposal.txt
- SI507project_db.py
- SI507_final_databases.sqlite (this will become a sample file)
- metro_export.csv (this will become a sample file)
- db.py
- advanced_expiry_caching.py
- database_schema_diagram


## I did not touch anything below this as I want to wait until I complete the assignment
---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
