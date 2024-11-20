# We can reverse a string by using different methods (loops)

# Using Slicing---------------------------
text1 = "Python"
reversed_text = text1[::-1]
print(reversed_text)


# Using For Loop:-------------------------------
text2 = "Python"
reversed_text = ""
for char in text2:
    reversed_text = char + reversed_text
print(reversed_text)


# Using While Loop:-------------------------------
text3 = "Python"
reversed_text = ""
i = len(text3) - 1
while i >= 0:
    reversed_text += text3[i]
    i -= 1
print(reversed_text)  # Output: nohtyP