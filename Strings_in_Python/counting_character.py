# How to count a specific word/character in string 

# Word Counter using loop ----------------------------------


def word_counter(string, target):
    target = target.lower().strip()
    string = string.lower().strip()
    counter = 0

    for char in string:
        if char == target:
            counter += 1

    return f"The word '{target}' is {counter} times in the given string."

words = "This is a string which is to be counted."
target = "i"
answer = word_counter(words, target)
print(answer)


# Word Counter using count method ----------------------------------

# How to count a specific word/character in string 

def word_counter(string, target):
    target = target.lower().strip()
    string = string.lower().strip()

    words = string.split()
    counter = words.count(target)

    return f"The word '{target}' is {counter} times in the given string."


words = "This is a string which is to be counted."
target = "is"
answer = word_counter(words, target)
print(answer)