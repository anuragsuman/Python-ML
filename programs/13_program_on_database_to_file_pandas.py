"""
Get data database
and write to
db_dump_3.txt
db_dump_4.csv
db_dump_5.xlsx
db_dump_6.json
db_dump_7.xml
db_dump_8.html
"""

# -------------
# Split into smaller tasks
# -------------
# Task-1: Get data from database - keep it in variable
# Task-2: Write database data to files
############################

print("# Task-1: Get data from database - keep it in variable")
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

print("Execute Select Query")
my_query = "SELECT * FROM MY_DATA_TABLE"
my_db_cursor.execute(my_query)
print("Done\n\n")

print("Database data")
my_db_result = my_db_cursor.fetchall()
print(my_db_result)
print("Done\n\n")

print("#"*40, end="\n\n")
###########################

print("Create DataFrame Object with DB data")
print("-"*20)
# ------------

import pandas as pd
my_db_data_df = pd.DataFrame(my_db_result, columns=["IP", "DATE", "PICS", "URL"])
print(my_db_data_df)

print("#"*40, end="\n\n")
###########################

print("# Task-2: Write database data to files")
print("-"*20)
# ------------

# db_dump_3.txt
my_db_data_df.to_csv("db_dump_3.txt", sep="\t") # default sep=","

# db_dump_4.csv
my_db_data_df.to_csv("db_dump_4.csv")

# db_dump_5.xlsx
my_db_data_df.to_excel('db_dump_5.xlsx', sheet_name="MyDBData")

# db_dump_6.json
my_db_data_df.to_json("db_dump_6.json")

# db_dump_7.xml
my_db_data_df.to_xml('db_dump_7.xml')

# db_dump_8.html
my_db_data_df.to_html('db_dump_8.html')

print("""
Below reports are created

db_dump_3.txt
db_dump_4.csv
db_dump_5.xlsx
db_dump_6.json
db_dump_7.xml
db_dump_8.html

please check
""")

print("#"*40, end="\n\n")
###########################