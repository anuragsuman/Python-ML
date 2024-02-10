"""
Get data from website
extract
IP
pics
and write extracted data to files
"""

# -------------
# Split into smaller tasks
# -------------
# Task-1: Read website data - keep it in variable
# Task-2: Parse log data using Beautifulsoup
# Task-3: Extract Info - Keep this in variable
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

print("# Task-3: Extract Info - Keep this in variable")
print("-"*20)
# ------------

# Store something like
# [ip, img, ip, img, ip, img]
# OR
# [[ip, img], [ip, img], [ip, img]]
# OR
# [(ip, img), (ip, img), (ip, img)]
extracted_info = []
for each_line in list_of_lines:
    if each_line.startswith("123"):
        sp = each_line.split()
        ip = sp[0]
        raw_img = sp[6]  # '/pics/wpaper.gif'
        # if raw_img.endswith("jpg") or raw_img.endswith("png")
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"
        each_line_tuple = (ip, img)
        extracted_info.append(each_line_tuple)

print(extracted_info)

print("#"*40, end="\n\n")
###########################

print("# Task-4: Write extracted info to file")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_txt_file_handle = open("web_report.txt", "w")
my_csv_file_handle = open("web_report.csv", "w")

# Step-2: Write
# ------------
# write heading to txt file
# my_txt_file_handle.write("IP\tPICS\n")
# my_txt_file_handle.writelines(["IP\t", "PICS\n"])
print("IP", "PICS", sep="\t", file=my_txt_file_handle, flush=True)

# write heading to csv file
# my_csv_file_handle.write("IP,PICS\n")
# my_csv_file_handle.writelines(["IP,", "PICS\n"])
print("IP", "PICS", sep=",", file=my_csv_file_handle, flush=True)

# 1-way
# extracted_info = [(ip, img), (ip, img), (ip, img)]
# for each_value_tuple in extracted_info:
#     print(each_value_tuple[0], each_value_tuple[1], sep="\t", file=my_txt_file_handle, flush=True)
#     print(each_value_tuple[0], each_value_tuple[1], sep=",", file=my_csv_file_handle, flush=True)

# 2-way
# extracted_info = [(ip, img), (ip, img), (ip, img)]
for i, j in extracted_info:
    print(i, j, sep="\t", file=my_txt_file_handle, flush=True)
    print(i, j, sep=",", file=my_csv_file_handle, flush=True)

# Step-3: Disconnect
# ------------
my_csv_file_handle.close()
my_txt_file_handle.close()

print("""
web report created successfully. Please check
web_report.txt
web_report.csv
""")

print("#"*40, end="\n\n")
###########################