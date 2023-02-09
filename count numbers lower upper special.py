def count_char(str1):
    upper_ctr = 0
    lower_ctr = 0
    number_ctr = 0
    special_ctr = 0
    for i in str1:
        if  <= ord(i) <=  :
            number_ctr += 1
        elif i.isupper():
            upper_ctr += 1
        elif i.islower():
            lower_ctr += 1
        else:
            special_ctr += 1
        return (f"no of uppercase ={upper_ctr}\nno of lowercase = {lower_ctr}\nno of number = {number_ctr}\nno of special char = {special_ctr}")
print(count_char("samyak12@#41"))
