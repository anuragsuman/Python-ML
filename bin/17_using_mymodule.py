"""
In this program, we are using
    variables, functions and classes available in mymodule.py
"""

print("about 'import'")
print("-"*20)
# ------------

from bin.mypackage.db import mymodule, mymodule as mm

# - import will create ONE EMPTY OBJECT 'mymodule'
# - It will execute 'mymodule.py'
# - When we execute 'mymodule.py', below 3 objects are getting created
#   1) course
#   2) log_process_kw_arg_func
#   3) MyLogProcessClass
# - import will keep all 3 objects inside brandnew 'mymodule' object

print("#"*40, end="\n\n")
###########################

print("1-way to 'import'")
print("-"*20)
# ------------

# Access string object
print("Course:", mymodule.course, sep="\n", end="\n\n")

# Access Function
func_result = mymodule.log_process_kw_arg_func(log_file_path=r"../log/server_log.txt")
print("func_result:", func_result, sep="\n", end="\n\n")

# Access Class
my_log_file_class_object = mymodule.MyLogProcessClass(r"../log/server_log.txt")
ips = my_log_file_class_object.get_ips()
print("ips_from_class:", ips, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("2-way to 'import'")
print("-"*20)
# ------------

# Access string object
print("Course:", mm.course, sep="\n", end="\n\n")

# Access Function
func_result = mm.log_process_kw_arg_func(log_file_path=r"../log/server_log.txt")
print("func_result:", func_result, sep="\n", end="\n\n")

# Access Class
my_log_file_class_object = mm.MyLogProcessClass(r"../log/server_log.txt")
ips = my_log_file_class_object.get_ips()
print("ips_from_class:", ips, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("3-way to 'import'")
print("-"*20)
# ------------

from bin.mypackage.db.mymodule import course, log_process_kw_arg_func, MyLogProcessClass

# Access string object
print("Course:", course, sep="\n", end="\n\n")

# Access Function
func_result = log_process_kw_arg_func(log_file_path=r"../log/server_log.txt")
print("func_result:", func_result, sep="\n", end="\n\n")

# Access Class
my_log_file_class_object = MyLogProcessClass(r"../log/server_log.txt")
ips = my_log_file_class_object.get_ips()
print("ips_from_class:", ips, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("4-way to 'import'")
print("-"*20)
# ------------

from bin.mypackage.db.mymodule import course as cs, log_process_kw_arg_func as lpf, MyLogProcessClass as LPC

# Access string object
print("Course:", cs, sep="\n", end="\n\n")

# Access Function
func_result = lpf(log_file_path=r"../log/server_log.txt")
print("func_result:", func_result, sep="\n", end="\n\n")

# Access Class
my_log_file_class_object = LPC(r"../log/server_log.txt")
ips = my_log_file_class_object.get_ips()
print("ips_from_class:", ips, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("5-way to 'import'")
print("-"*20)
# ------------


from bin.mypackage.db.mymodule import *

# Access string object
print("Course:", course, sep="\n", end="\n\n")

# Access Function
func_result = log_process_kw_arg_func(log_file_path=r"../log/server_log.txt")
print("func_result:", func_result, sep="\n", end="\n\n")

# Access Class
my_log_file_class_object = MyLogProcessClass(r"../log/server_log.txt")
ips = my_log_file_class_object.get_ips()
print("ips_from_class:", ips, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################