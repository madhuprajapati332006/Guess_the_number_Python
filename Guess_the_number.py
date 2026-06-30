# GUESS THE NUMBER (PROJECT) 
 
import random 

Target = random.randint(1,100)

while True:
    userChoice = (input("guess the target number os Quit: "))
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == Target):
        print("Success : Correct Guess!!")
        break

    elif(userChoice < Target):
        print("Your number was too small. Take a bigger guess....")

    else:
        print("Your number was too big. Take a smaller guess...")

print("----GAME OVER---")