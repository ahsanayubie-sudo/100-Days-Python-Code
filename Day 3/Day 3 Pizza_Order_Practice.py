print ("Wellcome to My pizza Shop")
pizza = input("What size of pizza you wan.t S,M or L ? ")
pepperoni = input ("you wan't pepperoni on your pizza y or n ? ")
extra_cheese = input ("You wan't extra_cheese cheese on your pizza y or n ? ")
bill = 0


if pizza == "s":
    bill += 30
elif pizza == "m":
    bill += 50  
else:
    bill += 70


if pepperoni == "y":
   bill += 10
   
if extra_cheese == "y":
    bill += 10
    
        
    
print (f"Your totel bill is {bill}")