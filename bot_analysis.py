from Bot import Bot
from random import randint
import numpy as np
import statistics
import itertools
import matplotlib.pyplot as plt


dice = []

# ----- EASY SCORE CLASS --------
class Score:
	def __init__(self):
		pass 

	def calculateScore(self, dice):
		score_max = 0

		# Calculates SUMS
		for x in range(1,6+1):
			score = dice.count(x) * x
			if score > score_max :
				score_max = score


		# LARGE STRAIGHT
		if (max(dice) - min(dice) + 1) == 4 and len(dice) == 5 :
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

for i in range(10):
	dice = []

	# Start position

	firstRoll()
	result = bot.solve(dice, score)
	print("Final score :" , result)
	results.append(result)

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
plt.plot(results[:,1], label="max score")
plt.plot(results[:,2], label="final score")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
