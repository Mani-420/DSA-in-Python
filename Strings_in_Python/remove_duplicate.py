# How to remove Duplicates from a string----------------
# By using For Loop-----------------------

word = "Web Developer"
result = ""

for char in word:
    if char not in result:
        result += char

print(result)


# By using While Loop-----------------------

word2 = "Web Developer"
result2 = ""
i = 0

while i < len(word2):
    if word2[i] not in result2:
        result2 += word2[i]
    i += 1

print(result2)

