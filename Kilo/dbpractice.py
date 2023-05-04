import json
import requests
import sqlite3
import os
from requests.auth import HTTPBasicAuth

# token = os.environ.get('v^1.1#i^1#I^3#p^1#r^0#f^0#t^H4sIAAAAAAAAAOVYXWwURRzv9dpa5EuSgsZUOVdIFNy92d373PQuXlugJ6Ut3FFKDZDZ3bl27X5ld9b2Gg2XBiigBJsY4wtShAfiA1ECIUJ8MAqJFjEaMICRGHmQGEn0Qb6Mxtm7Uq6VQKGX2MR92czM//M3/4+ZAbmqGUu2NW27PtvzSPlwDuTKPR52JphRVbl0jrf8ycoyUETgGc4tylUMeK/U2VBTTWENsk1Dt5GvT1N1W8hPxijH0gUD2oot6FBDtoAlIZVY1SxwDBBMy8CGZKiUL9kYo9goCodkwEqQDwUhipBZ/bbMtBGjYIQLBFgRyBkR8GLGXbdtByV1G0MdxygOcDwNgjTg02xY4IMCxzIcy3VSvnZk2YqhExIGUPG8uUKe1yqy9d6mQttGFiZCqHgysTzVmkg2LmtJ1/mLZMVHcUhhiB17/KjBkJGvHaoOurcaO08tpBxJQrZN+eMFDeOFConbxjyE+QWo+WA4jIAsR0Q5igLRkkC53LA0iO9thzujyHQmTyogHSs4ez9ECRriK0jCo6MWIiLZ6HN/qx2oKhkFWTFqWX1ifaKtjYq/5Opsgyoti6YFJazQqfoOOiTBaCYYykTogMiG5SDkRhUVpI3CPEFTg6HLigua7WsxcD0iVqOJ2HBF2BCiVr3VSmSwa1ExXfQ2hiDY6W5qYRcd3K27+4o0AoQvP7z/DoxxY2wpooPRmISJC3mISNqYpiJTExfzsTgaPn12jOrG2BT8/t7eXqaXZwyry88BwPo7VjWnpG6kQYrQurleoFfuz0AreVckRDhtRcBZk9jSR2KVGKB3UfEA4EI8O4r7eLPiE2f/NVHks398RpQqQxAMSCIXCHMBJIYDHCxFhsRHg9Tv2oFEmKU1aPUgbKpQQrRE4szRkKXIRFyG4yMZRMuhaIYORDMZWgzKIZrNIAQQEkUpGvk/JcpkQz2FJAvhksR6yeJ8OSuGTZROcEvbGpS2/p5Qz+pGtFqLrgP9utO0Su/vgCvaMXay/YnYZLPhrs43qApBJk30lwIAN9dLB0KTYWMkT8m9lGSYqM1QFSk7vTaYt+Q2aOFsvZMl4xRSVfKbkqsJ00yWpmKXzMkHLBYP53fpOtV/1KXu6pXtBu708srlt4kAaCoM6UNurmcZydD8BiSHEHd6U95q3wTCuxL5RSfLdDnIxsQSmZwDJ82kkGLOkJYmT56l0DCJE5NnIZcM2ZHwQynKd2aGoKl0dWP7gXT2TQUU0VF7Js8iI6hOKUQVctWYVgFKPC24rMiFOwKT95uxX5UYC9mGY5HrEdPqHpnTRg/SyQEEW4aqIqt9asnqll5NczAUVTTdanAJapFCct1zY5qdkNhQhCcXUp6bmm9S/vyzabp1kFJ3zge4CfnHv8vEy/IfO+D5BAx4Pi73eEAY0OxS8HyVd22FdxZlk9rD2FCXRaOPUWCGIWVPh9ixENODsiZUrPIqj3LxrHSj6EVoeAN4YuxNaIaXnVn0QARq76xUsnMfn83xIAh4NswHObYTPHtntYJdUFGjHVpz6jit7Q36Bk+dHN7/4Y1o6lEwe4zI46ksI+FbZlbN2vlr+sWfFx71OvNfO+3buPvYZ8ziNTd3tO7d413Obz5wuvpw94If57HPnPuhcu5IiC0b2rK1c3DPzC111+SRb3alw58OPbb1zBcnIt9eB6l5B95TVpypiVwxFg+dzR2p/u4tsbyvmldfH6nd9Xv/BfPcvsGPagLvtu84PqRfXL/jne1fD1068NO6E/7NK+u2Dz9XtjP3ZsOfT/UnY38cfLvp0vv7NlZeO781+cLQrY6d5zfH0M0vDw2Iv9xsXls+2FPTvGh+7f7aQ9XxXNXVy3+taI9lD7+8bGRe674tJ0ONc65/Pthy+be/FyrrPrhyYveRr75PLDkYuUC/seHqpaMr+73Hnq6V+25pdSOFbfwH7tOOKKsTAAA=')
# headers = {'Authorization': f'Token {token}'}
# url2 = 'https://api.ebay.com/oauth/api_scope'


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
    # f = open("responsestuff.html", "w")
    # f.write(content)
    # f.close()
    contentDict = json.loads(content)
    print()
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
        
        # records and prints SQLite version
        record = cur.fetchall()
        print(f'| SQLite version is {record}\t   |')
        print('--------------------------------------------\n')
        cur.close()

        # create table if table does not exist
        # Example 1: cur.execute("CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")
        cur.execute(f"CREATE TABLE IF NOT EXISTS {tableName} (id, callName, siteID, keywords, available)")
        # Example 3: cur.execute("CREATE TABLE temp_agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")

        # if table exists, prints table name  (currently no table exists)
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

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


main()








    # additional resources: 
    # SEC API:
    # data.sec.gov/submissions/
    # Each entity’s current filing history is available at the following URL:

# https://data.sec.gov/submissions/CIK##########.json
# Where the ########## is the entity’s 10-digit Central Index Key (CIK), including leading zeros.
    # open api keys: https://github.com/public-apis/public-apis
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


    # URL Haus API doc: https://urlhaus-api.abuse.ch/



# main()


fetchData()