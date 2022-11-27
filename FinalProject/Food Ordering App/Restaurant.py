#Food ordering App
import json
class Restaurant:
    def __init__(self):
        self.foods = {}
        self.food_id = len(self.foods)+1
        self.user_details = {}
        self.user_id = len(self.user_details)+1
        self.ordered_item=[]

    def add_food_items(self):
        print("**********************************************************************************************")
        print("**********************************************************************************************")
        self.name = input("Enter the Food Item Name: ")
        self.Quantity = int(input("Enter Food Quanitity: "))
        self.Price = int(input("Enter Food Price: "))
        self.Discount = int(input("Enter Discount: "))
        self.Stock = int(input("Enter Stock Value: "))
        self.item = {"name":self.name,"Quantity":self.Quantity,"Price":self.Price,"Discount":self.Discount,"Stock":self.Stock}
        self.food_id = len(self.foods)+1
        self.foods[self.food_id] = self.item
        print(self.item)
        print(self.foods)
        with open ("food_data.json","w") as f:
            json.dump(self.foods,f)
        print("!!  Item added successfully  !!\n")
 
    def edit_food_item(self):          
        x=int(input("Enter the Food ID you want to update "))
        if x in self.foods.keys():
            print("**********************************************************************************************")
            print(" 1. Update Food Name\n 2. Update Quantity\n 3. Update Price\n 4. Update Discount\n 5. Update Stock"  ) 
            print("**********************************************************************************************")
            y= int(input("Enter the number only: "))
            if y==1:
                self.foods[x]["name"]=input("Updated Food name :") 
                print(" !! Successfully Updated !!") 
            elif y==2: 
                self.foods[x]["Quantity" ]=int(input("Updated Quantity in values only: ")) 
                print(" !! Successfully Updated !!") 
            elif y==3: 
                self.foods[x][ "Price" ]=int(input("Updated Price in Rs only: ")) 
                print(" !! Successfully Updated !!") 
            elif y== 4 : 
                self.foods[x][ "Discount" ]=int(input( "Updated Discount in Rs only: "  )) 
                print(" !! successfully Updated !!") 
            elif y== 5 :
                self.foods[x][ "Stock" ]=int(input( "Updated Stock in values only: "  )) 
                print(" !! Successfully Updated !!") 
            else: 
                print(" !! Sorry Invalid Number !!")
        else:
            print(" !! Incorrect Food ID !!")
        with open ("food_data.json","w") as f:
            json.dump(self.foods,f)

    def view_food_item(self):
        print("**********************************************************************************************")
        print("**********************************************************************************************")
        print("!! Food item list are given below !!")
        with open('food_data.json') as f:
         data = json.load(f)
        print(data)
        print("**********************************************************************************************")
        print("**********************************************************************************************")
       
    def remove_food_items(self):
        x = int(input("Enter a Food id which you want delete: "))
        del self.foods[x]
        with open ("food_data.json","w") as f:
            json.dump(self.foods,f)
        print("!!  Item removed successfully  !!\n")

    def adminPanel(self):
        print("**********************************************************************************************")
        print("Press A -- FOR Add New Food Item ")
        print("Press B -- FOR Edit Food item ")
        print("Press C -- FOR View food Item ")
        print("Press D -- FOR Delete food Item ")
        print("***********************************************************************************************")
        option = input("Choose your Option: ")
        if option == "A" or option =="a":
            Restaurant.add_food_items(self)
        elif option == "B" or option =="b":
            Restaurant.edit_food_item(self)
        elif option == "C" or option == "c":
            Restaurant.view_food_item(self)
        elif option == "D" or option == "d":
            Restaurant.remove_food_items(self)
        else:
            pass

    def adminLogin(self):
        data = {}
        print("***** Admin login portal *****")
        name=input("please enter user name :")
        pwd=input("please enter password :")
        with open('login_information.json') as f:
            data = json.load(f)
        for p_id, p_info in data.items():
            if p_info['name']==name and p_info['Password']==pwd:
                print("!!  Login successful  !!")
                Restaurant.adminPanel(self)
            else:
                print("incorrect userid or password")

    def user_registration(self):
        self.name = input("Enter the user name: ")
        self.PhoneNumber = int(input("Enter Phone Number: "))
        self.Email = (input("Enter Email: "))
        self.Address = (input("Enter Address: "))
        self.Password = (input("Enter Password "))
        self.item = {"name":self.name,"PhoneNumber":self.PhoneNumber,"Email":self.Email,"Address":self.Address,"Password":self.Password}
        self.user_id = len(self.user_details)+1
        self.user_details[self.user_id] = self.item
        print(self.item)
        print(self.user_details)
        with open ("login_information.json","w") as f:
            json.dump(self.user_details,f)
        print("Registration successfull")

    def loginPortal(self):
        data = {}
        print("***** login portal *****")
        name=input("please enter user name :")
        pwd=input("please enter password :")
        with open('login_information.json') as f:
            data = json.load(f)
        #print(data)
        for p_id, p_info in data.items():
            if p_info['name']==name and p_info['Password']==pwd:
                print("!!  Login successful  !!")
                Restaurant.menufunction(self)
            else:
                print("incorrect userid or password")

    def menufunction(self):
        print("**********************************************************************************************")
        print("Press A -- FOR Place New Order ")
        print("Press B -- FOR Order History")
        print("Press C -- FOR Update Profile")
        print("***********************************************************************************************")
        option = input("Choose your Option: ")
        if option == "A" or option =="a":
            Restaurant.place_order(self)
        elif option == "B" or option =="b":
            Restaurant.order_history(self)
        elif option == "C" or option == "c":
            Restaurant.update_profile()
        else:
            pass

    def place_order(self):
        menu=[]
        print("**********************************************************************************************")
        print("!! Welcome !! \n list of Availabe Food Items:")
        for items in self.foods:
            menu.append([self.foods[items]["name"], self.foods[items]["Quantity"],self.foods[items]["Price"]]) 
        for i in range(len(menu)):
            print(i+1,menu[i])
        while True:
            print("**********************************************************************************************")
            x=int(input(" Enter 1 to Place the Order: \n Enter 2 to Exit: "))
            if x==1:
                print("**********************************************************************************************")
                print("\nEnter the Food number You want to order separated by comma, eg-1,2  :")
                y=input().split(",")
                for i in y:
                    z=int(i)
                    if z<=len(menu):
                        self.ordered_item.append(menu[z-1])
                    else:
                        print("We Don't have this Food Item: ")
                print("**********************************************************************************************")
                print("!! List of food item you selected !! ")
                for j in self.ordered_item:
                    print(j)
            elif x==2:
                break
            else:
                print("!! Invalid Number !!")

    def order_history(self):
        print("**********************************************************************************************")
        print(" !! List of Previous order !!")
        for i in self.ordered_item:
            print(i)

    def update_profile(self):
        print("Select Below Options to Update Your Profile Details")
        print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit")
        x=input()
        if x=="1":
            self.user_details["name"]=input("Enter your updated full name : ")
            print("\n!! Detail Updated Successfully !!")
        elif x=="2":
            self.user_details["PhoneNumber"]=int(input("Enter your updated 10 digit phone number : "))
            print("\n!! Detail Updated Successfully !!")      
        elif x=="3":
            self.user_details["Email"]=input("Enter your updated email id : ")
            print("\n!! Detail Updated Successfully !!")
        
        elif x=="4":
            self.user_details["Address"]=input("Enter your updated Address : ")
            print("\n!! Detail Updated Successfully !!")
        
        elif x=="5":
            self.user_details["Password"]=input("Enter your updated Password ")
            print("\n!! Detail Updated Successfully !!")

        elif x=="6":
            pass
        else:
            print("\\n!! Invalid Number Entered !!")
        
        if x in ["1","2","3",'4',"5"]:
            for i in self.user_details:
                print(i, ":",self.user_details[i])
                with open ("login_information1.json","w") as f:
                    json.dump(self.user_details,f)
                #print("Registration successfull")
        else:
            print("\\nPlease Enter correct Input")
      

    def main(self):
        print("**********************************************************************************************")
        print("**********************************************************************************************")
        print("!!  Welcome to Food Odering App  !!")
        print("Press A -- FOR Login as Admin ")
        print("Press B -- FOR Login as User ")
        option = input("Choose your Option: ")
        if option == "A" or option =="a":
            print("Press 1 -- FOR Login as Admin ")
            print("Press 2 -- FOR new Admin Registration ")
            option1 = input("Choose your Option: ")
            if option1 == "1":
                Restaurant.adminLogin(self)
            else:
                Restaurant.user_registration(self) 
        elif option == "B" or option =="b":
            print("Press 1 -- FOR Login as Existing User ")
            print("Press 2 -- FOR new user Registration ")
            option1 = input("Choose your Option: ")
            if option1 == "1":
                Restaurant.loginPortal(self)
            else:
                Restaurant.user_registration(self)  
        else:
            pass


#class Restaurant object creation 
obj = Restaurant()
obj.main()
#obj.add_food_items()
#obj.view_food_item()
#obj.edit_food_item()
#obj.view_food_item()
#obj.remove_food_items()
#obj.view_food_item()
#obj.adminPanel()
#obj.adminLogin()
#obj.user_registration()
#obj.loginPortal()
#obj.menufunction()
#obj.place_order()
#obj.order_history()
#obj.update_profile()