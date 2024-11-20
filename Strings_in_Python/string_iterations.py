# We can iterate through the strings by using multiple methods (loops)

# Using For Loop:
text1 = "Python"
for char in text1:
    print(char)


# Using While Loop:
text2 = "Python"
i = 0
while i < len(text2):
    print(text2[i])
    i += 1


# Using indices (enumerate):
text = "Python"
for index, char in enumerate(text):
    print(f"Index {index}: {char}")
