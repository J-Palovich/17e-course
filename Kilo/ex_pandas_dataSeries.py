#########################################################################################################


import pandas as pd
import numpy as np

# Pandas program to create and display a one-dimensional 
# array-like object containing an array of data using Pandas module

# ds = pd.Series([2, 4, 6, 8, 10])
# print(ds)

#########################################################################################################

# Write a Pandas program to convert a Panda module Series to Python list and it’s type
# .toList() method converts array or sinilar type into a list 

# ds = pd.Series([2, 4, 6, 8, 10])
# print("Pandas Series and type")
# print(ds)
# print(type(ds))
# print("Convert Pandas Series to Python list")
# print(ds.tolist())
# print(type(ds.tolist()))

#########################################################################################################

# Write a Pandas program to add, subtract, multiple and divide two Pandas Series

# import pandas as pd
# ds1 = pd.Series([2, 4, 6, 8, 10])
# ds2 = pd.Series([1, 3, 5, 7, 9])
# ds = ds1 + ds2
# print("Add two Series:")
# print(ds)
# print("Subtract two Series:")
# ds = ds1 - ds2
# print(ds)
# print("Multiply two Series:")
# ds = ds1 * ds2
# print(ds)
# print("Divide Series1 by Series2:")
# ds = ds1 / ds2
# print(ds)

# for i in ds1:
#     for j in ds2:
#         print(f'{i} + {j} = {i+j}') 

#########################################################################################################

# Write a Pandas program to compare the elements of the two Pandas Series

# ds1 = pd.Series([2, 4, 6, 8, 10])
# ds2 = pd.Series([1, 3, 5, 7, 10])
# print("Series1:")
# print(ds1)
# print("Series2:")
# print(ds2)
# print("\nCompare the elements of the said Series:")
# print("Equals:")
# print(ds1 == ds2)
# print("Greater than:")
# print(ds1 > ds2)
# print("Less than:")
# print(ds1 < ds2)

#########################################################################################################

# Write a Pandas program to convert a dictionary to a Pandas series

# d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
# print("Original dictionary:")
# print(d1)
# newSeries = pd.Series(d1)
# print("Converted series:")
# print(newSeries)

#########################################################################################################

# Write a Pandas program to convert a NumPy array to a Pandas series

# npArray = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print('numpy array:')
# print(npArray)
# newSeries = pd.Series(npArray)
# print('Converted Pandas Series:')
# print(newSeries)

#########################################################################################################

# Write a Pandas program to change the data type of given a column or a Series
# Changes number to float and errors on string

# series1 = pd.Series(['100', '200', 'pyton', '300.12', '400'])
# print('Original Data Series:')
# print(series1)
# print('Change data type to numeric')
# series2 = pd.to_numeric(series1, errors='coerce')
# print(series2)

#########################################################################################################

# Write a Pandas program to convert the first column of a DataFrame as a Series

# d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
# df = pd.DataFrame(data=d)
# print('Original DataFrame')
# print(df)

# series1 = df.first_valid_index[:,0]
# print('\nFirst Column as a Series:')
# print(series1)
# print(type(series1))

#########################################################################################################

# Write a Pandas program to display all the records of REGIONS file

employees = pd.read_csv(r"pandasCSVFiles/EMPLOYEES.csv")
departments = pd.read_csv(r"pandasCSVFiles/DEPARTMENTS.csv")
job_history = pd.read_csv(r"pandasCSVFiles/JOB_HISTORY.csv")
jobs = pd.read_csv(r"pandasCSVFiles/JOBS.csv")
countries = pd.read_csv(r"pandasCSVFiles/COUNTRIES.csv")
regions = pd.read_csv(r"pandasCSVFiles/REGIONS.csv")
locations = pd.read_csv(r"pandasCSVFiles/LOCATIONS.csv")

# reads and prints regions file from the above files using relative path

# print("All the records from regions file:\n")
# print(regions)
# print()

#########################################################################################################

# Write a Pandas program to display all the location id from locations file

# result = locations[['location_id']]
# print("\nAll the locations id from locations file:\n")
# print(result) 

#########################################################################################################

# Write a Pandas program to extract first 7 records from employees file.

# Equivalent SQL Syntax:
# SELECT  * FROM EMPLOYEES limit 7; 

# print("\nFirst 7 records from employees file:")
# print(employees.head(7))

#########################################################################################################

# Write a Pandas program to select distinct department id from employees file

# Equivalent SQL Syntax:
# SELECT DISTINCT department_id FROM EMPLOYEES;

# print("Distinct departmentID:")
# print(employees.department_id.unique())

#########################################################################################################

# Write a Pandas program to display the first and last name, and department number for all employees whose 
# last name is "McEwen".

# SELECT first_name, last_name, department_id
#  FROM employees
#   WHERE last_name = 'McEwen';

# print("Last name  First name    Department ID")
# result = employees[employees.last_name == 'McEwen']
# for index, row in result.iterrows():	
#     print(row['last_name'],'   ',row['first_name'],'       ',row['department_id'])

#########################################################################################################

# Write a Pandas program to display the first, last name, salary and department number for those 
# employees whose first name starts with the letter 'S'

# SELECT first_name, last_name, salary,  department_id
#   FROM employees
#    WHERE first_name  LIKE 'S%';

# print("First name       Last name      Salary    Department ID")
# result = employees[employees['first_name'].str[:1]=='S']
# for index, row in result.iterrows():
#     print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])

#########################################################################################################

# Write a Pandas program to display the first, last name, salary and department number for those 
# employees whose first name does not contain the letter 'M'.

# SELECT first_name, last_name, salary,  department_id
#   FROM employees
#    WHERE first_name NOT LIKE '%M%';

# print("\nLast name       First name      Salary    Department ID")

# result = employees[employees['first_name'].str.find('M')==-1]
# for index, row in result.iterrows():
#     print(row['last_name'].ljust(15),row['first_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])

#########################################################################################################
#  Write a Pandas program to display the first name, last name, salary and department number 
# in ascending order by department number

# SELECT first_name, last_name, salary,  department_id
#   FROM employees
#    ORDER BY department_id;

# print("First name       Last name      Salary    Department ID")
# result = employees.sort_values('department_id', ascending=True)
# for index, row in result.iterrows():
#     print(row['first_name'].ljust(15),row['last_name'].ljust(15),str(row['salary']).ljust(9),row['department_id'])

#########################################################################################################





#########################################################################################################




#########################################################################################################



































































