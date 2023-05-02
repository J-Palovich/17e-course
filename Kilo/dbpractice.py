import json
import requests
import sqlite3




def fetchData():
    #Acquire and transform the data, prepare variables for use in the for loop
    url = ("https://open.api.ebay.com/shopping?"
                            "callname=FindProducts&"
                            "responseencoding=JSON&"
                            "siteid=0&"
                            "version=967&"
                            "QueryKeywords=harry%20potter&"
                            "AvailableItemsOnly=true&"
                            "MaxEntries=2")
    response = requests.get(url)
    
    content = response.text
    contentDict = json.loads(content)
    # productList = contentDict[""][""]



def main():
    #creates SQLite database connetion to database that resides in memory 
    # con = sqlite3.connect(':memory:')
    tableName = 'products'

    try:
        #Automatically create and connect to the database
        con = sqlite3.connect('dbpractice.db')
        print('\n--------------------------------------------')
        print('| Database created and connected to SQLite |')
        selectQuery = 'Select sqlite_version()'

        #Create a cursor (an object that selects data in and operates on the table)
        cur = con.cursor()
        cur.execute(selectQuery)

        # if table exists, prints table name  (currently no table exists)
        # cur1.execute("SELECT name FROM sqlite_master WHERE type='table';")
        
        # records and prints SQLite version
        record = cur.fetchall()
        print(f'| SQLite version is {record}\t   |')
        print('--------------------------------------------\n')
        cur.close()

        # create table if table does not exist
        # Example 1: cur.execute("CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")
        cur.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (id, callName, siteID, keywords, available)")
        # Example 3: cur.execute("CREATE TABLE temp_agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")


        #Clears all data from table, columns will not be deleted. The cur.execute statements are SQL(Structured Query Langauge) commands.
        #SQL is the main language used to communicate with databases. Most data breaches occur because of a SQL-based vulnerability like SQL injection/SQLi.
        cur.execute("SELECT * FROM products")
        cur.execute("DELETE FROM products")

        fetchData()

    except sqlite3.Error as error:
        print('\nError while connecting to sqlite')

    finally:
        if (con):
            con.close()
            print('\nThe SQLite connection is closed.')











    # additional resources: 
    # https://www.w3resource.com/python-exercises/sqlite/python-sqlite-exercise-3.php

    # eBay APIs: https://developer.ebay.com/Devzone/shopping/docs/CallRef/FindProducts.html#Samples
    #   FindProducts: https://open.api.ebay.com/shopping?
    #    callname=FindProducts&
    #    responseencoding=XML&
    #    siteid=0&
    #    version=967&
    #    QueryKeywords=harry%20potter&
    #    AvailableItemsOnly=true&
    #    MaxEntries=2 




# main()


fetchData()