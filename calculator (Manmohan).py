def InputNumber():
    return int(input("Enter next number:"))
def Askoperation():
    return int(input("Add-1 , sub-2 ,mult-3 , divide-4"))
def Add(a,b):
    return a + b
def subract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
opt = Askoperation()
if opt == 1:
    print(Add(InputNumber(),InputNumber()))
elif opt == 2:
    print(subtarct(InputNumber(),InputNumber()))
elif opt == 3:
    print(multiply(InputNumber(),InputNumber()))
elif opt == 4:
    print(divide(InputNumber(),InputNumber()))
else:
    print("Invalid")
