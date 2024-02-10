"""
Requirement:
Extract
IP
PICS
from the given string

Expected Output:
-----------------
123.123.123.123
wpaper.gif
-----------------
"""

print("How input data looks like?")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(in_string)

print("#"*40, end="\n\n")
###########################

print("How input data looks like in RAW FORMAT?")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(repr(in_string))

print("#"*40, end="\n\n")
###########################

print("What type of data it is?")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(in_string))

print("#"*40, end="\n\n")
###########################

print("Methods inside 'str' class which we can use it to get EXPECTED OUTPUT")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(dir(in_string))

print("#"*40, end="\n\n")
###########################

print("Extract IP: 1-Way: IT WILL NOT WORK FOR ALL IP")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = in_string[0:15]
print(ip)

print("#"*40, end="\n\n")
###########################

print("Extract IP: 2-Way")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

# 1-way: WONT WORK
# end_index = in_string.index('3')

# 2-way
end_index = in_string.index(" ") # 1st space index
ip = in_string[0:end_index]
print(ip)

# COMMENT
# >>> s = "Hello"
# >>> s.index('H')
# 0
# >>> s.index('e')
# 1
# >>> s.index('l')
# 2
# >>>
# >>> s.index('l', 3) # Start looking from 3rd index onwards
# 3


print("#"*40, end="\n\n")
###########################

print("Extract IP: 3-Way")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = in_string.split()
print(sp, end="\n\n")

ip = sp[0]
print(ip)

# COMMENT
# >>> s = "WEL COME"
# >>> s.split() # SPLIT BY SPACE
# ['WEL', 'COME']
# >>> s.split('E')
# ['W', 'L COM', '']


print("#"*40, end="\n\n")
###########################

print("Extract PICS: 1-Way")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

# start_index = in_string.index('w') # WONT WORK
# start_index = in_string.index('/') # WONT WORK
# start_index = in_string.index('gif') # BIT DIFFICULT. KEEPING ON HOLD
start_index = in_string.index('/pics/') # Index of 1st / from '/pics/'
start_index = start_index + 1

# 1-way
end_index = in_string.index(" ", start_index)

# 2-way
end_index = in_string.index("HTTP") # index of 'H' we will get
end_index = end_index - 1


img = in_string[start_index:end_index]
print(img)


print("#"*40, end="\n\n")
###########################

print("Extract PICS: 2-Way")
print("-"*20)
# ------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = in_string.split()
print(sp, end="\n\n")


raw_img = sp[6] # '/pics/wpaper.gif'

# 1-way: Remove /pics/ from '/pics/wpaper.gif'
img_1 = raw_img[6:]

# 2-way: Remove /pics/ from '/pics/wpaper.gif'
raw_img_sp = raw_img.split("/")
print(raw_img_sp) # ['', 'pics', 'wpaper.gif']
img_2 = raw_img_sp[2]
img_3 = raw_img_sp[-1]

# 3-way: Remove /pics/ from '/pics/wpaper.gif'
start_index = raw_img.rindex("/")
start_index = start_index + 1
img_4 = raw_img[start_index:]

# 4-way: Remove /pics/ from '/pics/wpaper.gif'
img_5 = raw_img.lstrip('/pics/') # Default it will remove extra spaces\n\t from the beginning of the string
print(img_1, img_2, img_3, img_4, img_5, sep="\n")

# COMMENT
# s = "WEL COME"
# >>> s.rindex('E')
# 7
# >>> s.rindex('E', 6)
# 7
# >>> s.rindex('E', 2)
# 7

print("#"*40, end="\n\n")
###########################