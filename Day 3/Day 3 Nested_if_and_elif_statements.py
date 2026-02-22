#Nested_if_statements_and_elif_statements


print(" welcome to the rollarcoaster ")
height = int(input("What is your hight in cm? "))


if height >= 120:
    print("you can ride the rollercoaster" )
    age = int(input("What is your age") )
    if age >=12:
        print("Pay $12")
    elif age >= 18:
        print("Pay $7")
    else:
        print("Pay $12")    
else:
    print("Your are smale for this ride")