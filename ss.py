s = str(input())
s.lower()
new_str = ""
vowels = ['a','e','i','o','u']
for i in s:
    if i in vowels:
        new_str += "(" + i +")"
    else:
        new_str += i
print(new_strn)
    
