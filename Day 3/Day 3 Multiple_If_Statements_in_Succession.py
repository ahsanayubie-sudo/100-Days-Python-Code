  # Multiple_If_Statements_in_Succession

print(" welcome to the rollarcoaster ")
height = int(input("What is your hight in cm? "))
bill = 0 

if height >= 120:
    print("you can ride the rollercoaster" )
    age = int(input("What is your age") )
    if age >=12:
        bill = 5
        print("You need to pay ")
    elif age >= 18:
         bill =7
         print("You need to pay ")
    else:
         bill =12
         print("You need to pay ")
    photo = input("you Wan't photo  y or no ")
    if photo == "y":
        bill += 3
        print (f"your total Bill is {bill}")
            
else:
    print("Your are smale for this ride")