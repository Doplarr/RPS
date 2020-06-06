from random import randint

##Scoring System

Score = []
cpu_Score = []

#Choices for Player and CPU

choice = ["Rock", "Paper," "Scissors"]
cpu = choice[randint(0,2)]

#Start of a loop

player = False

#Game Start

while player == False:
    player = input("Rock, Paper, Scissors? \n")

##best 2 out of 3 wins.

    if len(Score) >= 2:
        print("Player has won!")
    elif len(cpu_Score) >= 2:
        print("Computer has won!")
    else:

##Continuing the game after checking for points.


##Making a tie

        if player == cpu:
            print("Tie!")

##Player Chooses Rock

        elif player == "Rock":
            if cpu == "Paper":
                print("You lose", cpu, "covers", player)

#Computer gains a point

                cpu_Score.append(1)
                if len(cpu_Score) > 1:
                    print("CPU has", len(cpu_Score), "points")
                else:
                    print("CPU has", len(cpu_Score), "point")

##Player gains a point

            else:
                print("You win", player, "Crushes", cpu)
                Score.append(1)
                if len(Score) > 1:
                    print("Player has", len(Score), "points")
                else:
                    print("Player has", len(Score), "point")

##Player Chooses Paper

        elif player == "Paper":
            if cpu == "Scissors":
                print("You lose", cpu, "Cuts", player)

#Computer gains a point

                cpu_Score.append(1)
                if len(cpu_Score) > 1:
                    print("CPU has", len(cpu_Score), "points")
                else:
                    print("CPU has", len(cpu_Score), "point")
            else:
                print("You win", player, "Covers", cpu)

#player gains a point

                Score.append(1)
                if len(Score) > 1:
                    print("Player has", len(Score), "points")
                else:
                    print("Player has", len(Score), "point")

##Player Chooses Scissors

        elif player == "Scissors":
            if cpu == "Rock":
                print("You lose", cpu, "Crushes", player)

#Computer gains a point

                cpu_Score.append(1)
                if len(cpu_Score) > 1:
                    print("CPU has", len(cpu_Score), "points")
                else:
                    print("CPU has", len(cpu_Score), "point")
            else:
                print("You win", player, "Cuts", cpu)

##player gains a point

                Score.append(1)
                if len(Score) > 1:
                    print("Player has", len(Score), "points")
                else:
                    print("Player has", len(Score), "point")

##Player inputs anything but items in list.

        else:
            print("That was not a valid response, please try again \n")

        player = False
        cpu = choice[randint(0,2)]
