class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = 0
    def getName(self):
        #return self.__name
        print("Name\t:", self.__name)
    def setName(self,name):
        self.__name = name

    def getRollNumber(self):
        #return self.__name
        print("RollNumber:", self.__rollNumber)
    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber

a = Student()
a.setName(input("enter a  student name: "))
a.setRollNumber(int(input("enter a rollnumber: ")))
a.getName()
a.getRollNumber()