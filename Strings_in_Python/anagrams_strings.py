def anagrams_checker(string1, string2):

    string1 = string1.replace(" ", "").lower().strip()
    string2 = string2.replace(" ", "").lower().strip()
    
    return sorted(string1) == sorted(string2)


input_string1 = "The Eyes"
input_string2 = "They See"

result = anagrams_checker(input_string1, input_string2)

if result == True:
    print("These string are anagrams.")
else:
    print("These string are not anagrams.")