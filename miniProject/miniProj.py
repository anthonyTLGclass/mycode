#!/usr/bin/env python3

#need random library to utilize random int  generator
import random

RPS = ["rock", "paper", "scissors"]

def genRPS():
    output = RPS[random.randint(0, 2)]
    return output

def main():
    # Generate Computer choice
    Computer = genRPS()
    # Get User choice
    User= input("Enter Rock, Paper or Scissors:\n>")
    Userlow = User.lower()
    # Enter infinite loop 
    while True:
        # If User and Computer are the same then ask User to chose again
        if Userlow == Computer:
            print(f"Go again, Computer threw {Computer}")
            # Get User choice
            User= input("Enter Rock, Paper or Scissors:\n>")
            Userlow = User.lower()
            Computer = genRPS()
        else:
            match Computer:
                case "rock":
                    #do something
                    if Userlow == "paper":
                        print(f"You win! Computer threw {Computer}")
                    else:
                        print(f"News Flash Buddy, you lose!, Computer threw {Computer}")
    
                case "paper":
                    #do something
                    if Userlow == "scissors":
                        print(f"You win! Computer threw {Computer}")
                    else:
                        print(f"News Flash Buddy, you lose!, Computer threw {Computer}")
                        
                case "scissors":
                    #do something
                    if Userlow == "rock":
                        print(f"You win! Computer threw {Computer}")
                    else:
                        print(f"News Flash Buddy, you lose!, Computer threw {Computer}")
            
            #break out of while loop
            break


main()
