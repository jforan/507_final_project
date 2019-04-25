import unittest
import sqlite3
from SI507project_scrape import *


class Scrape_and_Clean(unittest.TestCase):

    def test_scraping(self):
        for i in master:
            self.assertEqual(len(i), 5)

        ## the data was scraping off wikipedia and ommitting part of it, this tests that the mechanism in place to counter that is working


    def test_cleaning(self):
        for i in metro_data:
            if i[0] is 'Tokyo':
                        self.assertEqual(i[1],'Japan')

        ## some of these had references at the end that made things look funny. testing that they were removed from each of the elements


class Caching(unittest.TestCase):

    def test_cache(self):
        self.assertTrue(program_cache,"Testing that cache_diction is a dictionary")


class Database(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("SI507_final_databases.sqlite")
        self.cur = self.conn.cursor()

    def test_cities_table(self):
        self.cur.execute("select city, country from cities where city = 'New York City'")
        data = self.cur.fetchone()
        self.assertEqual(data, ('New York City', 'United States'), 'Testing data that results from selecting city New York City')

    def test_systems_table(self):
        self.cur.execute("select * from systems")
        data = self.cur.fetchone()
        self.assertTrue(data, 'Testing that you get a result from making a query to the systems table')

        ## ensures the tables are created and have data in them



if __name__ == "__main__":
    unittest.main(verbosity=2)
