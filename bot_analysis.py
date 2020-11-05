from Bot import Bot
from random import randint
import numpy as np
import statistics
import itertools
import matplotlib.pyplot as plt
import collections
from Score import Score

dice = []

# ----- EASY SCORE CLASS --------
""""
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
"""

NUMBER_DICES = 5

def firstRoll():
	for i in range(NUMBER_DICES):
		dice.append(randint(1,6))

bot = Bot()

def play(msg=False):
	global dice

	score = Score()



	# Number of Rounds
	N = 13

	for i in range(N):
		dice = []
		firstRoll()
		start_dice = dice.copy()
		initial_score, initial_key = score.getMaxScore(dice)
		#print("Start : ", dice, initial_score)

		for j in range(3):
			# Start position
			result = bot.solve(dice, score, False)
			#print("Final score :" , result)

		final_score, final_key = score.chooseMaxScore(dice)

		if msg==True : print("ROUND # ", i, start_dice, initial_score, ">>>", dice, final_key, final_score )

		#results.append([initial_score, result[0], result[1]])

	#print(results)

	total_score = score.final_score()
	

	return total_score


# ------------ MAIN ---------------

results = []

# Number of Games
M = 3
print("BOT ANALYSIS FOR", M, "GAMES")

for m in range(M):

	total_score = play()
	results.append(total_score)
	print("> GAME # ",m,"| FINAL  SCORE : ", total_score)


results = np.array(results)

#print(results[:,1])
print('-------RESULTS----------')
mean_final = statistics.mean(results)
print("Mean final",mean_final)

plt.plot(results, label="final score")

#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
