class Point:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def sqSum(self):
        print("sum of numbers: ",self.num1**2+self.num2**2+self.num3**2)

num1 = int(input("enter a num:"))
num2 = int(input("enter a num:"))
num3 = int(input("enter a num:"))
a = Point(num1,num2,num3)
a.sqSum()

