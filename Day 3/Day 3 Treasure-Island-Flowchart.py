print("Welcome to treasure island. Your mission is to find the treasure.")
mission = input("You want to go L for Left and R for Right: ")

# Use .upper() to handle both lowercase and uppercase at once
if mission.upper() == "L":
    swim_or_wait = input("Swim or Wait? (S/W): ")
    
    if swim_or_wait.upper() == "W":
        which_door = input("Which door? Red (R), Blue (B), or Yellow (Y): ")
        
        if which_door.upper() == "Y":
            print("You win!")
        elif which_door.upper() == "R":
            print("Burned by fire. Game Over.")
        elif which_door.upper() == "B":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over. That door doesn't exist!")
    else:
        print("Attacked by trout. Game Over.")  
else:
    print("Fall into a hole. Game Over.")
      
    
    
    
