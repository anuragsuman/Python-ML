"""
About Pandas
- Pandas is one library like mymodule/mypackage
- Pandas has many functions, classes inside it
    - Few function names are: read_csv, read_json etc
    - Few class names are: Series, DataFrame, ExcelWriter etc
- DataFrame class is MAIN/IMPORTANT here
- It has methods related to tabular-data/csv-data/xlsx-data/db-data
    so, we can use this class to store/process tabular data
"""

print("Store the values and print the values: Example-1")
print("-"*20)
# ------------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30], [40, 50, 60]])
print(my_df)

print("#"*40, end="\n\n")
###########################


print("Store the values and print the values: Example-1")
print("-"*20)
# ------------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30], [40, 50, 60]])
print(my_df)

print("#"*40, end="\n\n")
###########################


print("Store the values and print the values: Example-2")
print("-"*20)
# ------------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df)

print("#"*40, end="\n\n")
###########################

print("Methods inside 'DataFrame' Class")
print("-"*20)
# ------------

print(dir(my_df))

print("#"*40, end="\n\n")
###########################