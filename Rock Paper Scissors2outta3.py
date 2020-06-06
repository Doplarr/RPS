from random import randint

##Scoring System

Score = []
cpu_Score = []

#Choices for Player and CPU

choice = ["Rock", "Paper", "Scissors"]
cpu = choice[randint(0,2)]

#Start of a loop

player = False

#funcion for score system

def score():
    if (player == "Rock" and cpu == "Paper") or (player == "Paper" and cpu == "Scissors") or (player == "Scissors" and cpu == "Rock"):
        cpu_Score.append(1)
        if len(cpu_Score) > 1:
            print("CPU has", len(cpu_Score), "points")
        else:
            print("CPU has", len(cpu_Score), "point")
    else:
        Score.append(1)
        if len(Score) > 1:
            print("Player has", len(Score), "points")
        else:
            print("Player has", len(Score), "point")


while player == False:
    player = input("Rock, Paper, Scissors? \n")

##best 2 out of 3 wins.

    if len(Score) >= 2:
        input("Player has won!, Press Enter to Close the Program.")
    elif len(cpu_Score) >= 2:
        input("Computer has won!, Press Enter to Close the Program.")
    else:

##Continuing the game after checking for points.


##Making a tie

        if player == cpu:
            print("Tie!")

##Player Chooses Rock

        elif player == "Rock":
            if cpu == "Paper":
                print("You lose,", cpu, "covers", player)
                score()
            else:
                print("You win,", player, "Crushes", cpu)
                score()

##Player Chooses Paper

        elif player == "Paper":
            if cpu == "Scissors":
                print("You lose", cpu, "Cuts", player)
                score()
            else:
                print("You win", player, "Covers", cpu)
                score()

##Player Chooses Scissors

        elif player == "Scissors":
            if cpu == "Rock":
                print("You lose,", cpu, "Crushes", player)
                score()
            else:
                print("You win,", player, "Cuts", cpu)
                score()

##Player inputs anything but items in list.

        else:
            print("That was not a valid response, please try again \n")

        player = False
        cpu = choice[randint(0,2)]
