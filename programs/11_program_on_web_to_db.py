"""
ReWrite 10th program to send
extracted data to database
"""

'''
How to communicate with any databases?
Program  <-Communicate using library->  Any databases(SQL/No-SQL)

Example:
Program  <-Communicate using library(cx_Oracle)->  Oracle databases
Program  <-Communicate using library(mysql.connector)->  MySQL databases
Program  <-Communicate using library(sqlite3)->  SQLIte databases
'''

'''
We need ONE database
- We can use SQLite database

How to create / communicate with SQLite database?
OPTION-1: Using SQLite software 
          https://sqlitebrowser.org/dl/
OPTION-2: Using python library sqlite3, we can create / communicate with SQLite database
        with using SQLite software.
'''

# -------------
# Split into smaller tasks
# -------------
# Task-1: Read website data - keep it in variable
# Task-2: Parse log data using Beautifulsoup
# Task-3: Extract Info Using Regular Expression - Keep this in variable
# Task-4: Write extracted info database
############################

print("# Task-1: Read website data - keep it in variable")
print("-"*20)
# ------------

import urllib.request as ur

# 1. Connect
# ------------
my_web_file_handle = ur.urlopen('https://www.jafsoft.com/searchengines/log_sample.html')

# 2. Read
# ------------
web_content = my_web_file_handle.read()

# 3. Close
# ------------
my_web_file_handle.close()

web_content = web_content.decode()
print(web_content)

print("#"*40, end="\n\n")
###########################

print("# Task-2: Parse log data using Beautifulsoup")
print("-"*20)
# ------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
log_data = soup.body.pre.text
list_of_lines = log_data.splitlines()
print(list_of_lines)


print("#"*40, end="\n\n")
###########################

print("# Task-3: Extract Info - Keep this in variable")
print("-"*20)
# ------------

import re

# [(ip, dt, img, url), (ip, dt, img, url), (ip, dt, img, url),(ip, dt, img, url),]
extracted_info = []
for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*(http[s]?://[a-z./A-Z_0-9]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        each_line_tuple = (ip, dt, img, url)
        extracted_info.append(each_line_tuple)

print(extracted_info)

print("#"*40, end="\n\n")
###########################

print("Create database and table")
print("-"*20)
# ------------

import sqlite3

print("Connect/Create database 'my_data_db.sqlite3'")
# my_db_connection = sqlite3.connect(":memory:") # In Memory Database
my_db_connection = sqlite3.connect('my_data_db.sqlite3')
print("Done\n\n")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n\n")

print("Create table if not exists")
my_query = '''
CREATE TABLE IF NOT EXISTS MY_DATA_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
'''
my_db_cursor.execute(my_query)
print("Done\n\n")

print("#"*40, end="\n\n")
###########################
print("1-WAY: Insert records")
print("-"*20)
# ------------

# extracted_info = [(ip, dt, img, url), (ip, dt, img, url), (ip, dt, img, url),(ip, dt, img, url),]
for i, j, k, l in extracted_info:
    my_query = f"INSERT INTO MY_DATA_TABLE VALUES('{i}', '{j}', '{k}', '{l}')"
    # f-> format: It replace {var_name} with value
    print("Executing Query:", my_query)
    my_db_cursor.execute(my_query)
    print("One Record Inserted", end="\n\n")

my_db_connection.commit()
print("All records are inserted. Please check the database")

print("#"*40, end="\n\n")
###########################

print("2-WAY: Insert records")
print("-"*20)
# ------------

my_query = "INSERT INTO MY_DATA_TABLE VALUES(?, ?, ?, ?)"
my_db_cursor.executemany(my_query, extracted_info)
my_db_connection.commit()
print("All records are inserted AGAIN. Please check the database")
my_db_connection.close()

print("#"*40, end="\n\n")
###########################