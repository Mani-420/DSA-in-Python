# Using Two Pointer Technique----------------------------------

def checker_palindrome(expression):
    pharase = expression.lower().replace(" ", "").strip()
    left = 0
    right = len(pharase)-1

    while left <= right:
        if pharase[left] != pharase[right]:
            return f"{pharase} is not a palindrome."
        else:
            left += 1
            right -= 1 
        
        if left == right:
            return f"{pharase} is a palindrome."

result = checker_palindrome("Madam")
print(result)
result = checker_palindrome("Hello")
print(result)
result = checker_palindrome("Reparer")
print(result)


# Using Sliceing Method----------------------------------

def palindrome_checker(word):
    word = word.lower().replace(" ", "").strip()
    checker = word[::-1]
    if word == checker:
        return f"{word} is a palindrome."
    else:
        return f"{word} is not a palindrome."

answer = palindrome_checker("madam")
print(answer)
answer2 = palindrome_checker("Racecar  ")
print(answer2)
answer3 = palindrome_checker("Hello")
print(answer3)