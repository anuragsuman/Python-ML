"""
Get data from database
and
write to files
db_dump_1.txt
db_dump_2.csv
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
print("# Task-2: Write database data to file")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_txt_file_handle = open("db_dump_1.txt", "w")
my_csv_file_handle = open("db_dump_2.csv", "w")

# Step-2: Write
# ------------
# write heading to txt file
# my_txt_file_handle.write("IP\tPICS\n")
# my_txt_file_handle.writelines(["IP\t", "PICS\n"])
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle, flush=True)

# write heading to csv file
# my_csv_file_handle.write("IP,PICS\n")
# my_csv_file_handle.writelines(["IP,", "PICS\n"])
print("IP", "DATE", "PICS", "URL", sep=",", file=my_csv_file_handle, flush=True)

# 1-way
# extracted_info = [(ip, img), (ip, img), (ip, img)]
# for each_value_tuple in extracted_info:
#     print(each_value_tuple[0], each_value_tuple[1], sep="\t", file=my_txt_file_handle, flush=True)
#     print(each_value_tuple[0], each_value_tuple[1], sep=",", file=my_csv_file_handle, flush=True)

# 2-way
# extracted_info = [(ip, img), (ip, img), (ip, img)]
for i, j, k, l in my_db_result:
    print(i, j, k, l, sep="\t", file=my_txt_file_handle, flush=True)
    print(i, j, k, l, sep=",", file=my_csv_file_handle, flush=True)

# Step-3: Disconnect
# ------------
my_csv_file_handle.close()
my_txt_file_handle.close()

print("""
web report created successfully. Please check
db_dump_1.txt
db_dump_2.csv
""")

print("#"*40, end="\n\n")
###########################