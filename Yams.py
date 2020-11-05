from random import randint
from Score import Score
import easygui

#Bonjour

#Salut

kept_dices = []

score = Score()

def roll_dices():
    rolled_dices = []
    for i in range(5 - len(kept_dices)):
        rolled_dices.append(randint(1, 6))
        print("Value of dice " + str(i + 1) + " : ", rolled_dices[i])
    return rolled_dices

def choose_dices(n, rolled_dices):
    remove_indices = []

    if n == 2 : # Prendre automatiquement les dés restants
        for i in range(len(rolled_dices)) :
            kept_dices.append(rolled_dices[i])
    else : # Chosir les dés souhaités
        value = -1
        while value != 0:
            try:
                value = int(easygui.enterbox("Choose the dice(s) to re-roll : "))
                if value == 0:
                    break
                elif value > len(rolled_dices) or value < 0:
                    print("Error : This dice doesn't exist")
                elif (value - 1) in remove_indices:
                    print("Error : This dice is already chosen")
                else:
                    remove_indices.append(value - 1)
            except ValueError:
                print("Error : This is not a number")
            except TypeError:
                print("You left easygui") 
                exit()
        #kept_dices.append([i for j, i in enumerate(rolled_dices) if j not in remove_indices])
        for i in range(len(rolled_dices)):
            if i not in remove_indices:
                kept_dices.append(rolled_dices[i])
    print("Your dices are :", kept_dices, "\n")

# Main

print("\n----------[Yahtzee]----------")

for i in range(13):
    print("\nLaunch " + str(i + 1))
    kept_dices = []
    for n in range(3):
        print("(Type 0 when the selection is done)")
        rolled_dices = roll_dices()
        print("\n")
        choose_dices(n, rolled_dices)
    score.ask_score(kept_dices)
total = score.final_score()
print("\nYour final score is :", total)
