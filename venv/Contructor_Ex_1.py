class Person:
    def __init__(self,name):
        self.name = name
    def talk(self,value):
        print(f"My name is {self.name}")
        return value + 5


akshay = Person("Akshay Solanke")
print(akshay.talk(2))

Kiran = Person("Kiran Pardeshi")
Kiran.talk(1)

# Person is Class
# talk is an method of class
# akshay and Kiran are the objects of classmethod