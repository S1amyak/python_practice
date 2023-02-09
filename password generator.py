import random
letters = ['a','b','c','d','e','f','j','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
symbols = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['1','2','3','4','5','6','7','8','9','0']
password_list = []
letters_c = int(input("How many letters you want?"))
symbols_c = int(input("how many symbols you want?"))
numbers_c = int(input("how many numbers you want?"))
for i in range(1,letters_c + 1):
    password_list.append(random.choice(letters))
for j in range(1,symbols_c + 1):
    password_list.append(random.choice(symbols))
for k in range(1,numbers_c + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
print(f"your password is: {password}")
