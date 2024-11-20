# Strings in Python
# Strings are sequences of characters enclosed in single quotes ('), double quotes ("), 
# or triple quotes (''' or """). They are used to represent text data.

# Immutability of Strings
# In Python, strings are immutable, meaning their contents cannot be changed after creation. 
# Any operation that appears to modify a string (like concatenation or replacement) actually creates 
# a new string, leaving the original string unchanged.


# Concatenation in Strings------------------------------
# String concatenation is the process of joining two or more strings together to form a new string. 
# In Python, this can be done using the + operator or string interpolation methods.

# (+) Operator----
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)

# f-string--------
name = "Mithu"
greeting = f"Hello, {name}!"
print(greeting)


# Repetition of Strings (str * n)------------------------
# In Python, the * operator allows you to repeat a string multiple times. This operation creates a new string 
# by repeating the original string n times, where n is a non-negative integer.
text = "Hi! "
result = text * 3
print(result) 


# Slicing in Strings ------------------------------------
# Slicing in Python allows you to extract a portion (substring) of a string using a specified range of 
# indices. The syntax uses square brackets [] and a colon :.

text = "Hello, World!"
print(text[0:5])

text2 = "Python"
print(text2[:3])  
print(text2[3:]) 

text3 = "Python"
print(text3[-6:-3])

text4 = "abcdef"
print(text4[::2])  
print(text4[::-1]) 

