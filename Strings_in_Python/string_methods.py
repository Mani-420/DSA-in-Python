# String Methods in Python


# .find()---------------------
# Finds the first occurrence of a substring. Returns -1 if not found.
text1 = "Hello, World!"
print(text1.find("World"))  # Output: 7
print(text1.find("Python"))  # Output: -1


# .index()--------------------
# Finds the first occurrence of a substring. Raises an error if not found.
text2 = "Hello, World!"
print(text2.index("World"))  # Output: 7
# print(text2.index("Python"))  # Raises ValueError: substring not found


# .upper()--------------------
# Converts all characters to uppercase.
text3 = "hello"
print(text3.upper())  # Output: HELLO


# .lower()--------------------
# Converts all characters to lowercase.
text4 = "HELLO"
print(text4.lower())  # Output: hello


# .strip()--------------------
# Removes leading and trailing whitespace (or specified characters).
text5 = "   Hello, World!   "
print(text5.strip())  # Output: Hello, World!


# .replace()--------------------
# Replaces occurrences of a substring with another substring.
text6 = "I like Python"
print(text6.replace("Python", "Mern"))  # Output: I like Mern


# .split()
# Splits a string into a list of substrings based on a delimiter.
text7 = "apple,banana,cherry"
print(text7.split(","))  # Output: ['apple', 'banana', 'cherry']


# .join()
# Joins elements of an iterable (e.g., list) into a single string using a specified delimiter.
words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World
