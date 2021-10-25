Troubleshooting = input("Does it move?")

if (Troubleshooting == "yes") :
        Q1 = input("should it?")
        if (Q1 == "yes"):
            print("No Problem");
        elif (Q1 == "no") :
            print("Then use duct tape!!!");
        else :
            print("Answer my question! You didn't type yes or no.");


elif (Troubleshooting == "no") :
    Q2 = input("should it?")
    if (Q2 == "yes") :
        print("Then use WD-40")
    elif (Q2 == "no") :
        print("No problem")
    else :
        print("Answer my question! You didn't type yes or no.");
 
else:
    print("Answer my question! You didn't type yes or no.");