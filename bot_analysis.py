from Bot import Bot
from random import randint
import numpy as np
import statistics
import itertools
import matplotlib.pyplot as plt
import collections
from Score import Score

dice = []


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

		for j in range(2):
			# Start position
			result = bot.solve(dice, score, True) # Use bot.solve(dice, score, True) for round details
			#print("Final score :" , result)

		final_score, final_key = score.chooseMaxScore(dice)

		if msg==True : print("ROUND # ", i, start_dice, ":", initial_score, ">>>", dice, final_key, ":", final_score )

		#results.append([initial_score, result[0], result[1]])

	#print(results)

	total_score = score.final_score()
	

	return total_score


# ------------ MAIN ---------------

results = []

# Number of Games
M = 1
game_duration_expected = 14 # 17s for my laptop
print("BOT ANALYSIS FOR", M, "GAMES ( time expected to complete :" , (game_duration_expected*M) , "s )")

for m in range(M):

	total_score = play(True) # Use play(True) for game details
	results.append(total_score)
	print("> GAME # ",m,": FINAL  SCORE : ", total_score)


results = np.array(results)

#print(results[:,1])
print('-------RESULTS----------')
mean_final = statistics.mean(results)
print("Mean final",mean_final)

plt.plot(results, label="final score")

#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
