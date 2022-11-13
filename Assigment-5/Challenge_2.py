class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print("add to num:",self.num1+self.num2)
    def subtract (self):
        print("subtract to num:",self.num1+self.num2)
    def multiply (self):
        print("multiply to num:",self.num1*self.num2)
    def divide (self):
        print("divide to num:",self.num1/self.num2)

num1 = int(input("enter a num: "))
num2 = int(input("enter a num: "))     
obj = Calculator(num1,num2)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
