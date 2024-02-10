"""
Read and print website data
https://www.jafsoft.com/searchengines/log_sample.html
"""
print("type of website data")
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

print(type(web_content))

print("#"*40, end="\n\n")
###########################

print("Methods inside 'bytes' class")
print("-"*20)
# ------------


print(dir(web_content))

print("#"*40, end="\n\n")
###########################


print("Type After Converting to string")
print("-"*20)
# ------------

web_content = web_content.decode()

print(type(web_content))

print("#"*40, end="\n\n")
###########################


print("website content")
print("-"*20)
# ------------

print(web_content)

print("#"*40, end="\n\n")
###########################