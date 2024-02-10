"""
Requirement:
Get data from server_log.txt
THEN
Extract
IP
PICS
write extracted data to log_report.txt and log_report.csv

Expected Output in log_report.txt:
-----------------
    IP                  PICS
123.123.123.123     wpaper.gif
123.123.123.123     No Image
123.123.123.123     5star2000.gif
123.123.123.123     5star.gif
123.123.123.123     a2hlogo.jpg
123.123.123.123     No Image
-----------------

Expected Output in log_report.csv:
-----------------
    IP                  PICS
123.123.123.123,     wpaper.gif
123.123.123.123,     No Image
123.123.123.123,     5star2000.gif
123.123.123.123,     5star.gif
123.123.123.123,     a2hlogo.jpg
123.123.123.123,     No Image
-----------------

"""

# -----------------
# Split into smaller tasks
# -----------------
# Task-1: Read log file data and store in variable
# Task-2: Extract info and keep all extracted info in another variable
# Task-3: Write extracted info to file
###########################

print("# Task-1: Read log file data and store in variable")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_log_file_handle = open(r"../log/server_log.txt", "r")
#  - r"../log/server_log.txt" : while creating string
#   if we want to make raw string then prefix r''
#  - To convert existing string to raw string then use
#       repr()
# Step-2: Read
# ------------
file_content_in_list = my_log_file_handle.readlines()
print(file_content_in_list)

# Step-3: Disconnect
# ------------
my_log_file_handle.close()

print("#"*40, end="\n\n")
###########################
print("# Task-2: Extract info and keep all extracted info in another variable")
print("-"*20)
# ------------

# Store something like
# [ip, img, ip, img, ip, img]
# OR
# [[ip, img], [ip, img], [ip, img]]
# OR
# [(ip, img), (ip, img), (ip, img)]
extracted_info = []
for each_line in file_content_in_list:
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
print("# Task-3: Write extracted info to file")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_txt_file_handle = open("log_report.txt", "w")
my_csv_file_handle = open("log_report.csv", "w")

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
log report created successfully. Please check
log_reprot.txt
log_report.csv
""")

print("#"*40, end="\n\n")
###########################