# taking the user's input
medical = input("Do you have a medical cause: Y or N")
attendance = int(input("Enter the attendance of the student"))

if medical == "y":
    print("You are allowed")
else:
    if attendance >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")