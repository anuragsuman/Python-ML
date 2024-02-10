"""
Dump all
- 0 or more variables
- 0 or more functions definitions
- 0 or more Class definitions
here which we are planning to use in other programs
- This file also called
    PYTHON-MODULE or PYTHON-LIBRARY
"""

course = "Python"

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


class MyLogProcessClass:
    def __init__(self, log_file_path):
        my_log_file_handle = open(log_file_path, 'r')
        self.log_file_content = my_log_file_handle.readlines()
        my_log_file_handle.close()

    def get_ips(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                ip = sp[0]
                extracted_info.append(ip)
        return extracted_info

    def get_pics(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                raw_img = sp[6]  # '/pics/wpaper.gif'
                # if raw_img.endswith("jpg") or raw_img.endswith("png")
                if raw_img.startswith("/pics/"):
                    img = raw_img[6:]
                else:
                    img = "No Image"
                extracted_info.append(img)
        return extracted_info

    def get_both(self):
        extracted_info = []
        for each_line in self.log_file_content:
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



    def to_csv(self, out_file_path):
        # 1st Get extracted info
        log_result = self.get_both()

        # 2nd create and write to outfile
        my_out_file_handle = open(out_file_path, "w")
        print("IP", "PICS", sep=",", file=my_out_file_handle, flush=True)
        # log_result = [(ip, img), (ip, img), (ip, img)]
        for i, j in log_result:
            print(i, j, sep=",", file=my_out_file_handle, flush=True)
        my_out_file_handle.close()

    def to_txt(self, out_file_path):
        # 1st Get extracted info
        log_result = self.get_both()

        # 2nd create and write to outfile
        my_out_file_handle = open(out_file_path, "w")
        print("IP", "PICS", sep="\t", file=my_out_file_handle, flush=True)
        # log_result = [(ip, img), (ip, img), (ip, img)]
        for i, j in log_result:
            print(i, j, sep="\t", file=my_out_file_handle, flush=True)
        my_out_file_handle.close()

    def __add__(self, other): # self = x other=8080
        # 1st get all ips
        all_ips = self.get_ips()

        # 2nd add port to each ip
        all_ips_port = []
        for each_ip in all_ips:
            ip_with_port = each_ip + ":" + str(other)
            all_ips_port.append(ip_with_port)
        return all_ips_port
