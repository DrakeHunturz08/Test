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
	if (max(dice) - min(dice) + 1) == 4 and len(dice) == 5 :
		score = 40
		if score > score_max :
			score_max = score

	return score_max


NUMBER_DICES = 5

def firstRoll():
	for i in range(NUMBER_DICES):
		dice.append(randint(1,6))

def rerollDice(i):
	dice[i] = randint(1, 6)

# -------------- BOT CLASS -------------------------------


class Bot:
	def __init__(self):
		pass

	def solve(self, dice):
		initial_score = calculateScore(dice)
		print("Start : ", dice, initial_score)

		# First choice (roll 1 of the dices or not)
		best_choice = -1
		max_score = 0


		m = np.array(list(itertools.product([False, True], repeat=NUMBER_DICES)))
		#print(m)

		# FOR EVERY INPUT
		for i in range(len(m)):
			print("INPUT i=", i, m[i,:])
			#dice_copy = dice.copy()
			score_sum = 0
			count = 0

			p = (m[i,:] == True).sum()
			#print(p)

			# ------ FIND EVERY BRANCH POSSIBLE ------
			combinations = np.array(list(itertools.product(range(1,6+1), repeat= p)))
			#print("Combinations", combinations)

			kept_dices = []
			for j in range(len(m[i,:])):
				#print(j, m[i,j])
				if m[i,j] == False :
					kept_dices.append(dice[j])
			kept_dices = np.array(kept_dices)

			print("Kept Dices", kept_dices)


			#print("COMBINATIONS :")
			combinations_2 = []
			if len(combinations[0]) > 0 :
				for line in range(len(combinations)):
					#print(len(combinations[line]), len(kept_dices))
					if len(kept_dices) > 0:
						c = np.concatenate((combinations[line],kept_dices))
					else:
						c = combinations[line]
					#print(c)
					combinations_2.append(list(c))
			else :
				#print(kept_dices)
				combinations_2.append(list(kept_dices))


			# ------ EVALUATE EACH BRANCH AND CHOOSE BEST SCORE BY MEAN ------------

			score_sum = 0
			count = 0
			for comb in combinations_2 :
				count += 1
				score = calculateScore(comb)
				#print(comb, score)
				score_sum += score

			if count == 0 :
				score_mean = calculateScore(dice)
			else :
				score_mean = score_sum/count

			print("Score mean : ", score_mean)
			if score_mean > max_score :
				max_score = score_mean
				best_choice = i

		# ------ EXECUTE BEST INPUT CHOICE ------------


		print("Best choice : ", best_choice)

		if best_choice > -1 :
			for d in range(len(m[0])):
				if m[best_choice,d] == True :
					rerollDice(d)


		print(dice)
		final_score = calculateScore(dice)
		return [initial_score, max_score, final_score]


# ------------ MAIN ---------------
results = []

bot = Bot()

for i in range(10):
	dice = []

	# Start position

	firstRoll()
	result = bot.solve(dice)
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
