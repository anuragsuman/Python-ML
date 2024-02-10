"""
In this program, we are using
    variables, functions and classes available in some modules
    present inside some package
"""

'''
PACKAGES
- If want to develop more than one module then
    we can keep/organize those files inside folders or
    sub-folders
- These folders are called PACKAGES/SUB-PACKAGES
- we can directly import from package
'''

print("1-way to 'import'")
print("-"*20)
# ------------

import mypackage.db.mymodule

# Access string object
print("Course:", mypackage.db.mymodule.course, sep="\n", end="\n\n")

# Access Function
func_result = mypackage.db.mymodule.log_process_kw_arg_func(log_file_path=r"../log/server_log.txt")
print("func_result:", func_result, sep="\n", end="\n\n")

# Access Class
my_log_file_class_object = mypackage.db.mymodule.MyLogProcessClass(r"../log/server_log.txt")
ips = my_log_file_class_object.get_ips()
print("ips_from_class:", ips, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("2-way to 'import'")
print("-"*20)
# ------------

import mypackage.db.mymodule as mm

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

from mypackage.db.mymodule import course, log_process_kw_arg_func, MyLogProcessClass

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

from mypackage.db.mymodule import course as cs, log_process_kw_arg_func as lpf, MyLogProcessClass as LPC

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


from mypackage.db.mymodule import *

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
# ----------
# POINTS
# ----------
# If we are keeping mymodule.py and mypackage in some other directory/mountpoint
#   then put that path_to_directory in environment varaible
# Example: D:\mylib and E:\mymountdir\lib
# VARAIBLE NAME: PYTHONPATH
# VARAIBLE VALUE: D:\mylib,E:\mymountdir\lib
###########################
