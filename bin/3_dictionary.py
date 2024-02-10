"""
Dictionary
"""

print("Dictionary PART-1")
print("How to store and print")
print("-"*20)
# ------------

my_dictionary_1 = {0: "Java", 1: "Online", 2: 4}
# Internally it will create object of predefined class 'dict' and store the value

# OR we can also create using class name
my_dictionary_2 = dict({0: "Java", 1: "Online", 2: 4})

# If we keep key/value pair inside {} then it will become dictionary
# FOR KEY: We can use any IMMUTABLE VALUES like int, str, tuple etc
# FOR VALUE: It can be any type of value
my_dictionary_3 = {"course": "Java", "mode": "Online", "duration": 4}


my_dictionary_4 = {
    "duration": 4,
    "course": "Python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1,sep="\n", end="\n\n")
# default value for sep="ONE SPACE" # Between each value put ONE SPACE
# default value for end="\n"  # After printing all the values at the END put '\n'
# Total 4 arguments we can pass to print: 1) sep 2) end 3) file 4) flush
#   - 3) file and 4) flush: We will discuss during file operations

print("my_dictionary_2:", my_dictionary_2, sep="\n", end="\n\n")
print("my_dictionary_3:", my_dictionary_3, sep="\n", end="\n\n")
print("my_dictionary_4:", my_dictionary_4, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################
print("Dictionary PART-2")
print("How to store and print")
print("-"*20)
# ------------

my_dictionary = {
    "duration": 4,
    "course": "Python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

print("Duration:", my_dictionary["duration"], sep="\n", end="\n\n") # 4

print("Course:", my_dictionary["course"]) # "Python"
print("2nd character in Course:", my_dictionary["course"][1], sep="\n", end="\n\n") # "Python"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("2nd Mode:", my_dictionary["mode"][1]) # "offline"
print("2nd character in 2nd Mode:", my_dictionary["mode"][1][1], sep="\n", end="\n\n") # "f"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("Trainer FName:",my_dictionary["trainer"]["fname"]) # "abc"
print("2nd character in Trainer FName:", my_dictionary["trainer"]["fname"][1], sep="\n", end="\n\n") # "b"

print("#"*40, end="\n\n")
###########################

print("Dictionary PART-3")
print("List of methods")
print("-"*20)
# ------------

my_dictionary = {
    "duration": 4,
    "course": "Python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print(dir(my_dictionary))

print("#"*40, end="\n\n")
###########################