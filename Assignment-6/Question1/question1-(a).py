import json
class Employee:
    def createjson(self,*output):
    #print("data"+str(output))
        with open ("employee.json","w") as f:
            json.dump(output,f)
            print("Json Completed")

    def readjson(self):    
        with open('employee.json') as f:
            dataU = json.load(f)
            print(dataU)  

Names = ["William Studart", "Rishikesh Agrawani", "Tam Fransis", "Tom", "Sam"]
DOB = ["2018-2-5", "2017-7-5", "2016-5-2","2020-2-5","2000-2-7"]
Height = [6, 5,7,4,6]
City = ["Pune","Mumbai","Banglore","Chennai","Bhopal"]
State = ["Maharastra","Maharastra","Karnataka","TN","MP"]
output = [{"Name": d, "DOB": a, "Height": n, "City": c,"State":s} for d, a, n, c, s in zip(Names,DOB,Height,City,State)]

a=Employee()
a.createjson(*output)
a.readjson()
