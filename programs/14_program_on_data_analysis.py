"""
Data Analysis using pandas
"""

import pandas as pd

print("csv file content in df")
print("-"*20)
# ------------

csv_file_content_df = pd.read_csv("db_dump_4.csv")
print(csv_file_content_df)

print("#"*40, end="\n\n")
###########################


print("xlsx file content in df")
print("-"*20)
# ------------

excel_file_content_df = pd.read_excel("db_dump_5.xlsx")
print(excel_file_content_df)

print("#"*40, end="\n\n")
###########################

print("json file content in df")
print("-"*20)
# ------------

json_file_content_df = pd.read_json("db_dump_6.json")
print(json_file_content_df)

print("#"*40, end="\n\n")
###########################
print("All files content in one df")
print("-"*20)
# ------------

all_files_content_in_one_df = pd.concat([csv_file_content_df, excel_file_content_df, json_file_content_df], axis=0)
# axis=0: Merge vertically
print(all_files_content_in_one_df)
#all_files_content_in_one_df.to_csv("sample.csv")
print("#"*40, end="\n\n")
###########################


print("Column name")
print("-"*20)
# ------------

print(all_files_content_in_one_df.columns)
# ['Unnamed: 0', 'IP', 'DATE', 'PICS', 'URL']

print("#"*40, end="\n\n")
###########################


print("Remove Column 'Unnamed: 0'")
print("-"*20)
# ------------

all_files_content_in_one_df.drop(['Unnamed: 0'], axis=1, inplace=True)
# axis=1: Remove column
# axis=0: Remove row
print(all_files_content_in_one_df)

print("#"*40, end="\n\n")
###########################

all_files_content_in_one_df.to_csv("sample.csv", index=None)


print("Remove duplicate rows")
print("-"*20)
# ------------

all_files_content_in_one_df.drop_duplicates(inplace=True)
# inplace=True Means, make changes in same varaible i.e all_files_content_in_one_df
print(all_files_content_in_one_df)

print("#"*40, end="\n\n")
###########################
print("Add new column IP_WITH_PORT")
print("-"*20)
# ------------

all_files_content_in_one_df["IP_WITH_PORT"] = all_files_content_in_one_df["IP"] + ":8080"
print(all_files_content_in_one_df)

print("#"*40, end="\n\n")
###########################

print("List of columns")
print("-"*20)
# ------------

print(all_files_content_in_one_df.columns)
# ['IP', 'DATE', 'PICS', 'URL', 'IP_WITH_PORT']

print("#"*40, end="\n\n")
###########################

print("ReArrange the columns")
print("-"*20)
# ------------

print(all_files_content_in_one_df.columns)
all_files_content_in_one_df= all_files_content_in_one_df[['IP','IP_WITH_PORT', 'DATE', 'PICS', 'URL']]
print(all_files_content_in_one_df)

print("#"*40, end="\n\n")
###########################
print("Count of PICS column")
print("-"*20)
# ------------

print(all_files_content_in_one_df["PICS"].count())

print("#"*40, end="\n\n")
###########################


print("Value Count of PICS column")
print("-"*20)
# ------------

print(all_files_content_in_one_df["PICS"].value_counts())

print("#"*40, end="\n\n")
###########################

print("Show Value Count of PICS column in Graph")
print("-"*20)
# ------------


value_counts = all_files_content_in_one_df["PICS"].value_counts()
import matplotlib.pyplot as plt
value_counts.plot()

print("Please close the graph to continue the execution")
plt.show()

print("#"*40, end="\n\n")
###########################

print("Save Value Count Graph of PICS column in ")
print("-"*20)
# ------------


value_counts = all_files_content_in_one_df["PICS"].value_counts()
import matplotlib.pyplot as plt
plt.title("PICS Column Analysis")
plt.xlabel("Image Names")
plt.ylabel("Value Count")
value_counts.plot.bar()
plt.savefig("mygraph.png", bbox_inches='tight')

print("Graph 'mygraph.png' saved")

print("#"*40, end="\n\n")
###########################
all_files_content_in_one_df.to_csv("sample.csv", index=None)


print("Add data in sheet1 and graph in sheet2")
print("-"*20)
# ------------

# To work with single sheet we can use 'to_excel'
# To work with multiple sheets of same workbook
#   then use 'ExcelWriter' class present inside pandas library
my_writer_object = pd.ExcelWriter("final_report.xlsx", engine="xlsxwriter")
# engine: It supports multiple libraries, we can specify which library to use
# 'xlsxwriter' is of the library which we use

# Write data to default sheet
all_files_content_in_one_df.to_excel(my_writer_object, sheet_name="MyData", index=None)

# Add new sheet
new_sheet = my_writer_object.book.add_worksheet("MyGraph")

# Add image
# new_sheet.insert_image("Which Cell?", "image path")
new_sheet.insert_image("B2", "mygraph.png")

my_writer_object.close()

print("""Final Report
final_report.xlsx
created with the graph
please check
""")

print("#"*40, end="\n\n")
###########################