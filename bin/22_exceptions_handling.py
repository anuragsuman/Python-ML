"""
Exceptions Handling
"""

# print("Without handling exceptions")
# print("-"*20)
# # ------------
#
# a = 10
# b = 0
# result = a/b # Here program will terminate abruptly
# print("result:", result)
#
# print("#"*40, end="\n\n")
# ###########################

print("Handling exceptions")
print("-"*20)
# ------------

try:
    a = 10
    b = 0
    result = a/b # Here program will NOT terminate. Instead control passed to except block
    print("result:", result)
except:
    print("In Except")

print("#"*40, end="\n\n")
###########################


#  POINT-1
#####################
# try-except
# try-except-else
#   if try success then 'else' block and skip 'except' block
#   if try failed then 'except' block and skip 'else' block
# try-finally
##########################################

# POINT-2
#####################
# - all exceptions will be having classes
# - few are builtins
# - we can mention class name in except block
# - we can also write custom exception class
##########################################

print("Handling exceptions")
print("-"*20)
# ------------

try:
    a = 10
    b = 0
    result = a/b # Here program will NOT terminate. Instead control passed to except block
    print("result:", result)
except ZeroDivisionError:
    print("This is ZDE")
except NameError:
    print("This is NameError")
else:
    print("yaaaaa")

print("#"*40, end="\n\n")
###########################