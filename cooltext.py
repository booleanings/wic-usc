## The power of Python
#
# This program returns a given string as 1337sp3ak
# The dirty last line shows some of Python's principle idioms like string building and list comprehensions

text = input()
alphabet_leet = "48(D3F6#!JK1MN0PQR$7UVWXj2[ ]^_`48(d3f6#!jk1mn0pqr$7uvwxj2 "
print("".join([alphabet_leet[ord(x)-65 if (ord(x) > 65 and ord(x) < 122) else 58] for x in text]))

## Explanation
#
# text = input() <- gets user input, stores in variable text
#
# alphabet_leet = ... <- this is a string that contains our modified characters in relative order
#
# This is because if you were to get the ASCII characters for the normal alphabet ABCDE...wxyz, you would end up with a consecutive sequence like [65, 66, 67, 68, 69, ..., 119, 120, 121, 122]
# 
# Python comes with two useful functions for dealing with characters, ord() and chr(), which decode a character and encode a character respectively.
# EX: ord('A')=65 chr(65) = 'A'
#
# Breaking down the print() statement:
# "".join([...])
# The join command in Python conjoins elements of a list using a given string as glue.
# EX: "-".join[1,2,3] = "1-2-3"
# 
# The purpose of the join command here is to create a string from a list that we will generate based on the text given, explained below:
# 
# First we will start with the general idea:
# we want to generate a list that matches the string given, character by character, with our example modified string
# to do this, we will dynamically create a list, finding the proper matching indices and getting their corresponding characters with alphabet_leet[index]
# EX: If the user entered 'ABC', we would want to create a list that generates the values [0,1,2], since those correspond to the indices of our alphabet_leet string.
#
# An easy way of getting the index from the characters is to get its ASCII code and subtract it from 65 (the char code for capital A), so that 'A' will become 0, 'C' will become 2, and so on.
#
# To do this really easily for every character in the string, we use a list comprehension, which lets you build a list while iterating through another
# EX: [x*2 for x in [1,2,3]] = [2,4,6] 
# 
# Ours uses the method above, and also filters out any characters NOT within the ASCII spectrum defined above, such as $ (which has code 36)

