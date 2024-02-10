"""
Here
- conditional statement 'if'
- for-loop
- while-loop
"""

'''
In some languages we are using {} to make block like
if some_condn
{
s1
    s2
        s3
    s4
s5
}
s6

In python, we WONT use {} to make block, Instead we use INDENTATION
if some_condn_1:
    s1
    s2
    s3
    s4
    s5
    if some_condn_2:
        s1
        s2
        s3
        s4
        s5
s6
'''

print("Conditional statement 'if'")
print("-"*20)
# ------------

x = 10
s = "Python"
L = ["Java", 10, 12.3]
D = {"A": 10, "B":20}

if (x == 10) and ('th' in s) and ("Java" in L) and ("A" in D.keys()) and (('A', 10) in D.items()):
    print("x and s are equal")
elif x > 10:
    print("x is greater")
else:
    print("x is lesser")


# COMMENT
# >>> D = {"A": 10, "B":20}
# >>> dir(D)
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# >>>
# >>> D.keys()
# dict_keys(['A', 'B'])
# >>> D.values()
# dict_values([10, 20])
# >>> D.items()
# dict_items([('A', 10), ('B', 20)])

print("#"*40)
###########################
print("for-loop: Iterate any collection")
print("-"*20)
# ------------


s = "Python"
L = ["Java", 10, 12.3]
D = {"A": 10, "B":20}


# Syntax
# for provide_any_variable_name_here in provide_any_collection_here
for each_char in s:
    print("Each Char:", each_char)

for each_value in D.values():
    print("Value In DIctionary:", each_value)

# break: write this whenever we want to end the loop in between
# continue: write this whenever we want to jump to next iteration in between

print("#"*40)
###########################
print("while-loop: Execute loop based on condition")
print("-"*20)
# ------------


s = "Python"

D = {"A": 10, "B":20}

x = 0
while x < 5:
    print("Value of x is:", x)
    x = x + 1 # x += 1

L = ["Java", 10, 12.3]
index_value = 0
while index_value < len(L):
    print("Each Value In List:", L[index_value])
    index_value += 1

# break: write this whenever we want to end the loop in between
# continue: write this whenever we want to jump to next iteration in between

print("#"*40)
###########################