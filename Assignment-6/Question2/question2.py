#Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
class Dog:
    def __init__(self,name,age,coatcolor):
        self.name = name
        self.age = age
        self.coatcolor =coatcolor

    def description(self):
        print("Name:",self.name,"\n""Age:",self.age)

    def get_info(self):
        print("Color:",self.coatcolor)

class JackRussellTerrier(Dog):
    def description1(self,):
        super().description()
    def get_info1(self):
        super().get_info()
        
class Bulldog(Dog):
    def description2(self,):
        super().description()
    def get_info2(self):
        super().get_info()


a=JackRussellTerrier("Max","3year","Black")
a.description1()
a.get_info1()

b=Bulldog("sam","4year","red")
b.description2()
b.get_info2()

