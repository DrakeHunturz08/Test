from random import randint
import matplotlib.pyplot as plt
import numpy as np
import statistics
import itertools

dice = []

def calculateScore(dice):
	score_max = 0

	# Calculates SUMS
	for x in range(1,6+1):
		score = dice.count(x) * x
		if score > score_max :
			score_max = score


	# LARGE STRAIGHT
	if (max(dice) - min(dice) + 1) == 5 and len(dice) == 5 :
		score = 40
		if score > score_max :
			score_max = score

	return score_max


NUMBER_DICES = 2

def firstRoll():
	for i in range(NUMBER_DICES):
		dice.append(randint(1,6))

def rerollDice(i):
	dice[i] = randint(1, 6)


def play():
	global dice

	dice = []

	# Start position

	firstRoll()
	initial_score = calculateScore(dice)
	print("Start : ", dice, initial_score)


	# First choice (roll 1 of the dices or not)
	best_choice = -1
	max_score = 0


	m = np.array(list(itertools.product([False, True], repeat=NUMBER_DICES)))
	print(m)

	# FOR EVERY INPUT
	for i in range(len(m)):
		print(m[i,:])
		#dice_copy = dice.copy()
		score_sum = 0
		count = 0

		p = (m[i,:] == True).sum()
		#print(p)

		combinations = np.array(list(itertools.product(range(1,6+1), repeat= p)))
		print(combinations)

		kept_dices = []
		for j in range(len(m[i,:])):
			print(j, m[i,j])
			if m[i,j] == False :
				kept_dices.append(dice[j])

		print(kept_dices)


		for line in range(len(combinations)):
			print(size)
			if len(kept_dices) > 0:
				combinations[line] += kept_dices
			print(line, combinations[line])

		# FOR EVERY DICE
		"""
		for d in range(len(m[0])):

			# IF REROLL THIS DICE
			if m[i,d] == True :
				
				# FOR EVERY POSSIBLE DICE OUTCOME
				for j in range(1,6+1):
					count += 1
					dice_copy[d] = j
					score = calculateScore(dice_copy)
					print(dice_copy, score)
					score_sum += score
		"""

		if count == 0 :
			score_mean = calculateScore(dice)
		else :
			score_mean = score_sum/count
		print("Score mean : ", score_mean)
		if score_mean > max_score :
			max_score = score_mean
			#best_choice = d


	print("Best choice : ", best_choice)

	if best_choice > -1 :
		for d in range(len(m[0])):
			if m[i,d] == True :
				rerollDice(d)


	print(dice)
	final_score = calculateScore(dice)
	return [initial_score, max_score, final_score]


# ------------ MAIN ---------------
results = []

for i in range(1):
	result = play()
	print("Final score :" , result)
	results.append(result)

#print(results)

results = np.array(results)

#print(results[:,1])

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
#plt.show()
