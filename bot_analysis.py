from Bot import Bot
from random import randint
import numpy as np
import statistics
import itertools
import matplotlib.pyplot as plt
import collections


dice = []

# ----- EASY SCORE CLASS --------
class Score:
	def __init__(self):
		pass 

	def calculateScore(self, dice):
		score_max = 0
		counter = (collections.Counter(dice))

		# Calculates SUMS
		for x in range(1,6+1):
			score = dice.count(x) * x
			if score > score_max :
				score_max = score

		# THREE OF A KIND
		if dice.count(1) == 3 or dice.count(2) == 3 or dice.count(3) == 3 or dice.count(4) == 3 or dice.count(5) == 3 or dice.count(6) == 3:
			score = sum(dice)
			if score > score_max :
				score_max = score

		# FOUR OF A KIND
		if dice.count(1) == 4 or dice.count(2) == 4 or dice.count(3) == 4 or dice.count(4) == 4 or dice.count(5) == 4 or dice.count(6) == 4:
			score = sum(dice)
			if score > score_max :
				score_max = score

		# FULL HOUSE
		if len(counter) == 2 and (counter[list(counter.keys())[0]] == 2 or counter[list(counter.keys())[0]] == 3):
			score = 25
			if score > score_max :
					score_max = score


		# LARGE STRAIGHT
		if len(counter) == 5 and (max(dice) - min(dice)) == 4:
			score = 40
			if score > score_max :
				score_max = score

		return score_max


NUMBER_DICES = 5

def firstRoll():
	for i in range(NUMBER_DICES):
		dice.append(randint(1,6))


# ------------ MAIN ---------------
results = []

score = Score()

bot = Bot()

# Number of games
N = 10

for i in range(N):
	dice = []
	firstRoll()
	start_dice = dice.copy()
	initial_score = score.calculateScore(dice)
	#print("Start : ", dice, initial_score)

	for j in range(3):
		# Start position
		result = bot.solve(dice, score, False)
		#print("Final score :" , result)

	print("GAME # ", i, start_dice, initial_score, ">>>", dice, result[1] )

	results.append([initial_score, result[0], result[1]])

#print(results)

results = np.array(results)

#print(results[:,1])
print('-------RESULTS----------')
mean_initial = statistics.mean(results[:,0])
print("Mean initial", mean_initial)
mean_max = statistics.mean(results[:,1])
print("Mean max",mean_max)
mean_final = statistics.mean(results[:,2])
print("Mean final",mean_final)


plt.plot(results[:,0], label="initial score")
plt.plot(results[:,1], label="max mean score")
plt.plot(results[:,2], label="final score")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
