def longest_substring_checker(string):
    max_length = 0
    temp_string = ""
    max_string = ""
    temp_list = []

    string_length = len(string)

    for outer in range(string_length):
        for inner in range(outer, string_length):
            if string[inner] in temp_string:
                if len(temp_string) > max_length: 
                    max_length = len(temp_string)
                    max_string = temp_string
                temp_list.append(temp_string)
                temp_string = ""
                break
            else:
                temp_string += string[inner]
    
    return max_string


input_string = "abcabcdefgklamnopqarstu"
result = longest_substring_checker(input_string)
print(f"The longest string is :{result}")