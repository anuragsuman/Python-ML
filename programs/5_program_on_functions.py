"""
Write 4th program using functions.

Write function which takes log_file_path as an argument
then let it extract and return extracted information
"""

# -----------------
# Split into smaller tasks
# -----------------
# Task-1: Write function to extract info and return extracted info
# Task-2: Write extracted info to file
###########################

print("# Task-1: Write function to extract info and return extracted info")
print("-"*20)
# ------------


def log_process_pos_arg_func(log_file_path):
    """
    function which takes log_file_path as an argument
    then let it extract and return extracted information
    :param log_file_path:
    :return extracted_info:
    """
    # Get the data from log file
    # ------------
    my_log_file_handle = open(log_file_path, "r")
    file_content_in_list = my_log_file_handle.readlines()
    my_log_file_handle.close()
    # ------------
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
    return extracted_info


def log_process_kw_arg_func(*, log_file_path):
    """
    function which takes log_file_path as an argument
    then let it extract and return extracted information
    :param log_file_path:
    :return extracted_info:
    """
    # Get the data from log file
    # ------------
    my_log_file_handle = open(log_file_path, "r")
    file_content_in_list = my_log_file_handle.readlines()
    my_log_file_handle.close()
    # ------------
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
    return extracted_info


func_result_1 = log_process_pos_arg_func(r"../log/server_log.txt")
print("func_result_1:", func_result_1)

func_result_2 = log_process_kw_arg_func(log_file_path=r"../log/server_log.txt")
print("func_result_2:", func_result_2)

print("#"*40, end="\n\n")
###########################

print("# Task-2: Write extracted info to file")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_txt_file_handle = open("func_report.txt", "w")
my_csv_file_handle = open("func_report.csv", "w")

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
for i, j in func_result_1:
    print(i, j, sep="\t", file=my_txt_file_handle, flush=True)
    print(i, j, sep=",", file=my_csv_file_handle, flush=True)

# Step-3: Disconnect
# ------------
my_csv_file_handle.close()
my_txt_file_handle.close()

print("""
log report created successfully. Please check
func_report.txt
func_report.csv
""")

print("#"*40, end="\n\n")
###########################