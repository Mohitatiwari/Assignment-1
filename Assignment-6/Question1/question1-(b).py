
##  Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file

import json
name = {"State_Assam":"Capital_Dispur","State_Goa":"Capital_Panaji","State_Gujarat":"Capital_Gandhinagar","State_Nagaland":"Capital_Kohima","State_Sikkim":"Capital_Gangtok","State_Tripura":"Capital_Agartala","State_Madhya Pradesh":"Capital_Bhopal"} 
with open ("state.json","w") as f:
    json.dump(name,f)
    print("Json Completed")
with open('state.json') as f:
    dataU = json.load(f)
    print(dataU)  

