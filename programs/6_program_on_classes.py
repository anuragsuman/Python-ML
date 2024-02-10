"""
Write 6th program using classes
"""

# -----------------
# Split into smaller tasks
# -----------------
# Task-1: Write class to extract info and write to files
#       - 1. write method to extract ip
#       - 2. write method to extract pics
#       - 3. write method to extract both
#       - 4. write method to write to csv file
#       - 5. write method to write to txt file
###########################


print("# Task-1: Write class to extract info and write to files")
print("-"*20)
# ------------


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



my_log_file_class_object = MyLogProcessClass(r"../log/server_log.txt")
ips_list = my_log_file_class_object.get_ips()
print("ips_list:", ips_list, sep="\n", end="\n\n")

pics_list = my_log_file_class_object.get_pics()
print("pics_list:", pics_list, sep="\n", end="\n\n")

both_list = my_log_file_class_object.get_both()
print("both_list:", both_list, sep="\n", end="\n\n")

ips_with_port = my_log_file_class_object + 8080
print("ips_with_port:", ips_with_port, sep="\n", end="\n\n")

my_log_file_class_object.to_txt("class_report.txt")
print("file class_report.txt created.Please check")

my_log_file_class_object.to_csv("class_report.csv")
print("file class_report.csv also created.Please check")


print("#"*40, end="\n\n")
###########################