"""
File Operations:
Communicate(Read/Write) with external files :
Text files with any extension like .txt, .csv, .log, .mylog, .yourlog etc
Finally files which can be opened in notepad
"""

'''
We need to follow 3 steps for any read/write operations
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
'''

'''
We have functions for all 3 steps
Step-1: Connect to file
        - open() function
Step-2: Read/Write
        - For Write: 1) write 2) writelines 3) print function
        - For Read: 1) read 2) readline 3) for-loop to read line by line
                    4) readlines 5) list/tuple/set/dictionary classes to read
Step-3: Disconnect
        - flush() # Send data from buffer to file. It will not close FILE CONNECTION
        - close() # 1st it will call flush() then it will call close()
'''

print("All write operations")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
# my_file_handle = open("provide file name or file path here", "provide mode")
my_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only
# mode 'w': It will create new file
# mode 'w': IMPORTANT: It will erase the existing content if present

# Step-2: Write
# ------------

# Our data
x = 10
y = "Python\n"

# Convert other type of data to string. Because write & writelines expects
# data in strings
x = str(x) + "\n"

# 1) write : use this method if we have data in single string which we want to
#   write to file. So, write takes one string of any length
my_file_handle.write(x) # Send data to buffer
my_file_handle.write(y) # Send data to buffer
my_file_handle.flush() # Send data from buffer to file

# 2) writelines : use this method if we have data in any collection like list, tuple etc
#   which we want to write to file. So, writelines takes any  collection like list, tuple etc
my_data_in_list = [x, y]
my_file_handle.writelines(my_data_in_list)
my_file_handle.flush()

# 3) print function
# - no need to convert to string
# - no need to add '\n' as well
x = x.strip() # Removes spaces\n\t etc from both ends of the string
y = y.strip()
print(x, y, 20, "JAVA", sep="\n", end="", file=my_file_handle, flush=True)
# end="" : Empty so \n is not added after writing
# 20: no need to convert to string

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("""
All write operations are completed.
Please check 'my_out_file.txt'
""")

print("#"*40)
###########################
print("Read operations: 1) read()")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_file_handle = open("my_out_file.txt", "r")
# mode 'r': Read Only
# mode 'r': It will NOT create new file

# Step-2: read
# ------------
file_content = my_file_handle.read() # return complete file content in single string
print("file_content:", file_content)
print("file_content in RAW FORMAT:", repr(file_content))

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40)
###########################
print("Read operations: 2) readline()")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_file_handle = open("my_out_file.txt", "r")
# mode 'r': Read Only
# mode 'r': It will NOT create new file

# Step-2: read
# ------------
file_content = my_file_handle.readline()
print("1st Line:", file_content)

file_content = my_file_handle.readline()
print("2nd Line:", file_content)

file_content = my_file_handle.readline()
print("3rd Line:", file_content)

# Seek Pointer: Internally all read/write operations will
# make use of pointer called 'seek' to track
# - we can set to any character
# - 0 means 0th character, i.e beginning of the file

# Set seek to 0, i.e beginning of the file
my_file_handle.seek(0)
file_content = my_file_handle.readline()
print("1st Line:", file_content)

my_file_handle.seek(1)
file_content = my_file_handle.readline()
print("1st Line 2nd character onwards till end of the line:", file_content)

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40)
###########################
print("Read operations: 3) read line by line using for-loop")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_file_handle = open("my_out_file.txt", "r")
# mode 'r': Read Only
# mode 'r': It will NOT create new file

# Step-2: read
# ------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40)
###########################
print("Read operations: 4) readlines, list, tuple, set, dictionary")
print("-"*20)
# ------------

# Step-1: Connect to file
# ------------
my_file_handle = open("my_out_file.txt", "r")
# mode 'r': Read Only
# mode 'r': It will NOT create new file

# Step-2: read
# ------------
file_content = my_file_handle.readlines() # in list
print("file_content in using readlines():", file_content)
# Seek reached EOF

file_content = my_file_handle.readlines()
print("Empty Because seek reached EOF:", file_content)

# Set seek to 0
my_file_handle.seek(0)
file_content = list(my_file_handle)
print("file_content in list :", file_content)
# Seek reached EOF

# Set seek to 0
my_file_handle.seek(0)
file_content = tuple(my_file_handle)
print("file_content in tuple :", file_content)
# Seek reached EOF

# Set seek to 0
my_file_handle.seek(0)
file_content = set(my_file_handle)
print("file_content in set :", file_content)
# Seek reached EOF

# Set seek to 0
my_file_handle.seek(0)
file_content = dict(enumerate(my_file_handle))
print("file_content in dictionary :", file_content, sep="\n", end="\n\n")
# Seek reached EOF

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40)
###########################


# ------------
# Different Modes
##############
# mode 'w': Write Only, It will create new file, It erase the content
# mode 'r': Read Only, It will NOT create new file
# mode 'a': Append Only, It will create new file only if not present
# mode 'w+': RW, It will create new file, It erase the content
# mode 'r+': RW, It will NOT create new file
# mode 'a+': RW, It will create new file only if not present
#
# NOTE: RW- Means using same file handle we can call read as well as write methods
###########################