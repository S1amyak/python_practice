# To capitalize first and last letter

def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper()
    print(result)
capitalize_first_last_letters("samyak")
