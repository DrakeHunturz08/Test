import easygui 
import numpy 
import collections

class Score:

    def __init__(self):
        self.upper = {
            "Ones" : -1,
            "Twos" : -1,
            "Threes" : -1,
            "Fours" : -1,
            "Fives" : -1,
            "Sixes" : -1,
        }
        self.lower = {
            "Three of a kind" : -1,
            "Four of a kind" : -1,
            "Full house" : -1,
            "Small straight" : -1,
            "Big straight" : -1,
            "Yahtzee" : -1,
            "Chance" : -1,
        }
        self.score_total = 0

    def ask_score(self, kept_dices):
        index = 1
        for key, value in {**self.upper, **self.lower}.items():
            if value == -1:
                print(str(index) + " " + key)
                index += 1
        while 1:
            try:
                choice = int(easygui.enterbox("Choose your combinaison : "))
                if 0 < choice < index:
                    index2 = 1
                    for key, value in {**self.upper, **self.lower}.items():
                        if value == -1:
                            if index2 == choice:
                                variable = 0
                                if key in self.upper:
                                    variable = self.upper
                                elif key in self.lower:
                                    variable = self.lower
                                else:
                                    print("Vous êtes idiot")  

                                c
                                if score > -1:
                                    if score == 0:
                                        confirmation = easygui.ynbox("Are you sure to leave the " + key + " and scored 0 point ?")
                                        if confirmation == False:
                                            break
                                    variable[key] = score
                                    print("You choose the key " + key + " and scored " + str(variable[key]) + " points")
                                    return 
                                else:
                                    break
                            index2 += 1
                else:
                    print("Error : Number not in list")
            except ValueError:
                print("Error : Enter a number")
            except TypeError:
                print("You left easygui") 
                exit()

    def calculate(self, kept_dices, key):
        if key == 'Ones':
            if kept_dices.count(1) > 0:
                return kept_dices.count(1)
            else:
                return 0
        elif key == 'Twos':
            if kept_dices.count(2) > 0:
                return kept_dices.count(2) * 2
            else:
                return 0
        elif key == 'Threes':
            if kept_dices.count(3) > 0:
                return kept_dices.count(3) * 3
            else:
                return 0
        elif key == 'Fours':
            if kept_dices.count(4) > 0:
                return kept_dices.count(4) * 4
            else:
                return 0 
        elif key == 'Fives': 
            if kept_dices.count(5) > 0:
                return kept_dices.count(5) * 5 
            else:
                return 0 
        elif key == 'Sixes':   
            if kept_dices.count(6) > 0:
                return kept_dices.count(6) * 6
            else:
                return 0
        elif key == 'Three of a kind':
            if kept_dices.count(1) == 3 or kept_dices.count(2) == 3 or kept_dices.count(3) == 3 or kept_dices.count(4) == 3 or kept_dices.count(5) == 3 or kept_dices.count(6) == 3:
                return sum(kept_dices)
            else:
                return 0
        elif key == 'Four of a kind':
            if kept_dices.count(1) == 4 or kept_dices.count(2) == 4 or kept_dices.count(3) == 4 or kept_dices.count(4) == 4 or kept_dices.count(5) == 4 or kept_dices.count(6) == 4:
                return sum(kept_dices)
            else:
                return 0
        elif key == 'Full house':
            counter = (collections.Counter(kept_dices))
            if len(counter) == 2 and (counter[list(counter.keys())[0]] == 2 or counter[list(counter.keys())[0]] == 3):
                return 25
            else:
                return 0
        elif key == 'Small straight':
            counter = (collections.Counter(kept_dices))
            if len(counter) == 5 and (max(kept_dices) - min(kept_dices)) == 4:
                return 30
            elif len(counter) == 4 and (max(kept_dices) - min(kept_dices)) == 3:
                return 30
            elif len(counter) == 5 and 3 in kept_dices and 4 in kept_dices:
                return 30
            else:
                return 0
        elif key == 'Big straight':
            counter = (collections.Counter(kept_dices))
            if len(counter) == 5 and (max(kept_dices) - min(kept_dices)) == 4:
                return 40
            else:
                return 0
        elif key == 'Yahtzee':
            if kept_dices[0] == kept_dices[1] == kept_dices[2] == kept_dices[3] == kept_dices[4]:
                return 50
            else:
                return 0
        elif key == 'Chance':
            return sum(kept_dices)
        return -1 

    def getMaxScore(self, dices):
        score_max = 0
        key_max = ""
        for key, value in {**self.upper, **self.lower}.items(): 
            # If key is not taken yet
            if value == -1:
                score = self.calculate(dices, key)
                if score > score_max :
                    score_max = score
                    key_max = key

        return score_max, key_max

    def chooseMaxScore(self, kept_dices):
        score, key = self.getMaxScore(kept_dices)

        if key in self.upper:
            self.upper[key] = score
        elif key in self.lower:
            self.lower[key] = score

        return score, key

    def final_score(self):
        somme = 0
        for key in self.upper:
            if self.upper[key] > -1:
                somme += self.upper[key]
        if somme >= 63:
            print("Your Upper Section points are > 63, you have 35 bonus points.")
            somme += 35
        for key in self.lower:
            if self.lower[key] > -1:
                somme += self.lower[key]
        return somme
