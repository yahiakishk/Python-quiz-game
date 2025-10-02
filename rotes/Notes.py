# you can hold middle mouse button and scroll to type the same thing into multiple lines
#
# f-strings are cleaner then adding a "," or "+"
#
# input: for user input, it'll wait until the user inputs smth to run the rest of the code
#
# can type cast the input directly
# eg: int(input("how old are you"))
#
# augmented assignment operators
#
# eg:
# score = 0
# print(f"starting score is {score})
# Player collects coins
# score += 10
# print(f"score is {score})
#
# Player defeats an enemy
# score += 50
# print(f"after defeating an enemy, score is {score})
#
# result = abs(y) absolute value
# result = pow(x, 2) x to the power of
# result = round(x) rounds
# result = max(x,y,z) selects max
# result = min(x, y, z) selects min
#
# import math
# print(math.pi)
# print(math.e)
# result = math.sqrt(9)
# result = math.ceil(1.1) #to round up
# result = math.floor(1.9) to round down
#
# to round do
# round(123.1231231, 2) so first number is the number you wanna round and second is how much you wanna round it
#
# If statements: if --> run code if a condition is true,
#               else will do smth else
#
# elif is used when you want to check another condition after an if.
# Only runs if the previous if (or elif) was False and its own condition is True.
#
# == is for comparison
# != is for exception
#
# when doing round(result, 4) number of decimals must be in the parentheses
#
# .lower() at the end of an input command to make it accept uppercase
#
# x if condition else y
#
# find the first position of a letter or number within a string : example.find(e)
# find the last position of a letter or number within a string : example.rfind(e) [r is for reverse]
# find length of a string: len(example)
# to capitalize : example.capitalize()
# to make it all full caps : example.upper()
# to make it all lower case : example.lower()
# to check if all digits : example.isdigit() it gives a t or f, t only if all digits else false
# to check if all letters : example.isalpha() it gives a t or f, t only if all letters else false
# example.count(e) to count number of times a character gets repeated
# example.replace(e, E) to replace
#
# indexing is to access an element of a sequence, using [] [start : end : step]
# start is inclusive (will include 0) ending index is exclusive (will exclude the last number)
# i can also just not type 0 if im starting from the beginning eg [:9]
# if you wanna go till the end you can do this : [9:]
# if you need the last character you can do : [-1]
# [::3] step will print every third item for example and [::2] would print every second item, so on
# example[::-1] could be used to reverse it
#
# format specifiers:
# :.f2 Float with 2 decimals
# :02 pad with zero to 2 digits (eg: 01, 02, 03, ..., 10, 11)
# :.f0 Float rounded to integer
# :, Adds commas for thousands
# :.2% Converts to percentage with 2 decimals
# :e Scientific notation
# :b Binary
# :<10 Left-align in width 10
# :>10 Right-align in width 10
# :^10 Center in width 10
# :.5 Truncate to first 5 chars
#
# reversed.example() to reverse a string
#
# while in a for loop you can use break to break out of the loop
# and continue to skip a specific iteration of the loop
# eg: for x in range(1, 21):
#       if x == 13:
#         continue
#       else:
#         print(x)
#
# if counting downwards you can use range(10, 0, -1)
#
# only use range for counting in a range, else don't use it
# eg: cc_num = "1234-5678-9012-3456"
# for x in cc_num:
#  if x == "6":
#    break
#  else:
#    print(x)
#
# while in a loop, if i have a contiue i shouldn't do input("") cuz it'll ask for input twice, instead use print("")
# print(example, end="") to have it all in one line
#
# List = [] order and changable. ok to duplicate
# to find specific element: print(example[1])
#
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchagable. duplicats are ok. faster
#
# can use steps with collections  
# print help function if you forget what you can do 
# "example" in example_list {will show you if it's in the list and will return bool}

# example.append("example") to add to the end of a list
# example.remove("example") to remove from a list
# example.insert(0, "example") to insert at the beginning of a list
# example.sort() to sort a list alphabetically 
# example.reverse() to reverse a list (not alphabetically) but in reverse order)
# example.sort() then example.reverse() to sort in reverse alphabetical order
# example.clear to clear a list
# example.index("example") to find the index of an item in a list 
# (if it's not in the list it'll return an error)
# (if there are two of the same item it'll return the first one)
# if you wanna find the last one you can do example.reverse() then example.index("example"))
# example.count("example") to count how many times an item is in a list
# gotta make a nested sequence to remove the brackers and curly brackets
#
# 2d lists are lists within a list