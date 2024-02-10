"""
Read website url,
extract log data content from webpage
and print
"""

# -------------
# Split into smaller tasks
# -------------
# Task-1: Read website data - keep it in variable
# Task-2: Parse using Beautifulsoup
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

print("create object of BeautifulSoup class and print")
print("-"*20)
# ------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)

print("#"*40, end="\n\n")
###########################
print("Head Tag")
print("-"*20)
# ------------

print(soup.head)

print("#"*40, end="\n\n")
###########################


print("Body Tag")
print("-"*20)
# ------------

print(soup.body)

print("#"*40, end="\n\n")
###########################
print("Title tag")
print("-"*20)
# ------------

print(soup.head.title) #  <TITLE>A Web server log file explained</TITLE>

print("#"*40, end="\n\n")
###########################

print("Title tag Text")
print("-"*20)
# ------------

print(soup.head.title.text) #  A Web server log file explained

print("#"*40, end="\n\n")
###########################

print("1st Link tag")
print("-"*20)
# ------------

print(soup.head.link) # <LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">

print("#"*40, end="\n\n")
###########################

print("1st Link tag attributes")
print("-"*20)
# ------------

print("Link Tag: ", soup.head.link) # <LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">
print("REL:", soup.head.link.get('rel'))
print("HREF:", soup.head.link.get('href'))
print("TYPE:", soup.head.link.get('type'))

print("#"*40, end="\n\n")
###########################
print("All link tags")
print("-"*20)
# ------------

all_link_tags = soup.head.find_all('link')
print(all_link_tags)

print("#"*40, end="\n\n")
###########################

print("print each link tag and its attributes")
print("-"*20)
# ------------

for each_link_tag in all_link_tags:
    print("each_link_tag: ", each_link_tag)
    print("REL:", each_link_tag.get('rel'))
    print("HREF:", each_link_tag.get('href'))
    print("TYPE:", each_link_tag.get('type'), end="\n\n")

print("#"*40, end="\n\n")
###########################
print("Log data")
print("-"*20)
# ------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
###########################

print("type of Log data")
print("-"*20)
# ------------

log_data = soup.body.pre.text
print(type(log_data))

print("#"*40, end="\n\n")
###########################

print("Log data in RAW Format")
print("-"*20)
# ------------

log_data = soup.body.pre.text
print(repr(log_data))

print("#"*40, end="\n\n")
###########################

print("List of lines")
print("-"*20)
# ------------

log_data = soup.body.pre.text

# 1-way
# list_of_lines = log_data.split("\n")

# 2-way
list_of_lines = log_data.splitlines()

print(list_of_lines)

print("#"*40, end="\n\n")
###########################