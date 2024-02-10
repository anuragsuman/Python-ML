"""
Write 9th program using regular expression
- Use regular expression to extract information
"""

# -------------
# Split into smaller tasks
# -------------
# Task-1: Read website data - keep it in variable
# Task-2: Parse log data using Beautifulsoup
# Task-3: Extract Info Using Regular Expression - Keep this in variable
# Task-4: Write extracted info to file
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

print("# Regular Expression: Match Result")
print("-"*20)
# ------------

import re

for each_line in list_of_lines:
    match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("match_result:", match_result)

# COMMENT - 2
'''
Regular Expression

IDENTIFIERS
--------------
\d -> to represent any ONE digit b/n 0 to 9
\D -> to represent any ONE non-digit. Any character except 0 to 9
. -> to represent any ONE ANY character
\. -> Strictly DOT
[0-9]-> to represent any ONE digit b/n 0 to 9. Here we can specify different range of
        number
[0-255] -> It can be any number b/n 0 to 2 (OR) It can be 5
--------------

QUANTIFIERS
--------------
\d{3} -> Internally it will become \d\d\d
\d{1,3} -> Internally it will become (\d|\d\d|\d\d\d)
--------------

MODIFIERS
--------------
* -> It makes 0 or more times
+ -> It makes 1 or more times
? -> It makes 0 or 1 time
--------------

'''

# COMMENT - 1
'''
match_result = re.match("Provide pattern for IP address line", "Provide string here")

HOW IP ADDRESS LINE LOOKS LIKE?

FROM THE BEGINNING
1 to 3 digits then DOT
then
1 to 3 digits then DOT
then
1 to 3 digits then DOT
then
1 to 3 digits
then
SOME CHARACTERS ARE PRESENT TILL THE END
'''

print("#"*40, end="\n\n")
###########################
print("Extract IP")
print("-"*20)
# ------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)


# COMMENT
'''
- put () for IP address pattern
    '(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*'
- match function will capture - CALLED GROUP
- GROUP(0) will be having entire match
'''

print("#"*40, end="\n\n")
###########################
print("Extract IP, DATE")
print("-"*20)
# ------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT
'''
26/Apr/2000

Pattern for 26
---
\d\d # Strictly 2 numbers
\d{2} # Strictly 2 numbers
[0-9][0-9] # Strictly 2 numbers
\d[0-9] # Strictly 2 numbers
[0-9]\d # Strictly 2 numbers
[0-9]{2} # Strictly 2 numbers

\d{1,2} # Minimum one digit and maximum 2 digits
[0-9]{1,2} # Minimum one digit and maximum 2 digits
\d?\d # Minimum one digit and maximum 2 digits
[0-9]?[0-9] # Minimum one digit and maximum 2 digits
---

Pattern for 'Apr'
---
[a-zA-Z]{3}
[A-Z][a-z]{2}
(Jan|Feb|Mar)
---
'''
print("#"*40, end="\n\n")
###########################
print("Extract IP, DATE, PICS")
print("-"*20)
# ------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        print(ip, dt, img)

# COMMENT
'''
\s -> ONE SPace
\S -> Except SPACE, any character

(pics/([0-9a-z]+\.(gif|jpg)))?
Making above pattern is optional so that lines which
is not having pics will also be matched
'''

print("#"*40, end="\n\n")
###########################
print("Extract IP, DATE, PICS, URL")
print("-"*20)
# ------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST)\s+/(pics/([0-9a-z]+\.(gif|jpg)))?.*(http[s]?://[a-z./A-Z_0-9]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url)

# COMMENT
'''
http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

http[s]?://[a-z./A-Z_0-9]+

http[s]? -> s is optional
https? -> s is optional
(https)? -> https is optional
[https] -> any ONE character in this GROUP


'''

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
print("# Task-4: Write extracted info to file")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_txt_file_handle = open("regex_report.txt", "w")
my_csv_file_handle = open("regex_report.csv", "w")

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
for i, j, k, l in extracted_info:
    print(i, j, k, l, sep="\t", file=my_txt_file_handle, flush=True)
    print(i, j, k, l, sep=",", file=my_csv_file_handle, flush=True)

# Step-3: Disconnect
# ------------
my_csv_file_handle.close()
my_txt_file_handle.close()

print("""
web report created successfully. Please check
regex_report.txt
regex_report.csv
""")

print("#"*40, end="\n\n")
###########################