firstnumber = input("Girve me a number...") 
secondnumber = input("well, give me another number...") 
operation = input("And what operation do you want (mul, div, or mod)")  
if (operation == "mul") :
    print(firstnumber * secondnumber)  
 
elif (operation == "div") :
    print(firstnumber / secondnumber)  
 
elif (operation == "mode") :
    print(firstnumber % secondnumber)  
 
else:
    print("*** invalid operation *** ")  
 

