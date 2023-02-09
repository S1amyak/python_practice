# POLYMORPHISM  (MANY FORMS)
#print(len("cipherschools"))
#print(len([10,20,30,40]))

'''def sum(x,y,z=0):
    return x + y + z

print(sum(2,3))

print(sum(2,3,4))'''

'''class India():
    def Capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Muliple language is spoken in India")

class USA:
    def Capital(self):
        print("Washington DC")

    def language(self):
        print("English")


obj1 = India()
obj2 = USA()

obj1.Capital()
obj2.language()'''

class Bird:
    def intro(self):
        print("This is bird class")

    def flight(self):
        print("Birds fly")

class Parrot(Bird):
    def flight(self):
        print("Parrot can fly")


class Ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")


obj1 = Bird()
obj1.intro()
obj1.flight()

obj2 = Parrot()
obj2.intro()
obj2.flight()

obj3 = Ostrich()
obj2.intro()
obj3.flight()













































