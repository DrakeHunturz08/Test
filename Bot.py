from random import randint
import numpy as np
import statistics
import itertools


class Bot:
	def __init__(self):
		pass

	def rerollDice(self, dice, i):
		dice[i] = randint(1, 6)
		return dice

	def solve(self, dice, score,  msg=False):
	

		# First choice (roll 1 of the dices or not)
		best_choice = -1
		max_score = 0

		# ----- GET MATRIX OF POSSIBLE MOVES (2^5) -------
		m = np.array(list(itertools.product([False, True], repeat=len(dice))))
		#print(m)

		# --------- FOR EVERY INPUT -----------------
		for i in range(len(m)):
			if msg==True : print("INPUT i =", i, m[i,:])
			score_sum = 0
			count = 0

			p = (m[i,:] == True).sum()

			# ------ FIND EVERY BRANCH POSSIBLE ------
			combinations = np.array(list(itertools.product(range(1,6+1), repeat= p)))
			#print("Combinations", combinations)

			kept_dices = []
			for j in range(len(m[i,:])):
				#print(j, m[i,j])
				if m[i,j] == False :
					kept_dices.append(dice[j])
			kept_dices = np.array(kept_dices)

			#print("Kept Dices", kept_dices)


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


			# ------ EVALUATE EACH BRANCH AND CHOOSE BEST SCORE BY >>> AVERAGE/MEAN <<< ------------

			score_sum = 0
			count = 0
			for comb in combinations_2 :
				count += 1
				sc, key = score.getMaxScore(comb)
				#print(comb, sc)
				score_sum += sc

			if count == 0 :
				score_mean, key = score.getMaxScore(dice)
			else :
				score_mean = score_sum/count

			if msg==True : print("Score mean : ", score_mean)
			if score_mean > max_score :
				max_score = score_mean
				best_choice = i

		# ------ EXECUTE BEST INPUT CHOICE ------------


		if msg==True :print("Best choice : ", best_choice, m[best_choice,:])

		if best_choice > -1 :
			for d in range(len(m[0])):
				if m[best_choice,d] == True :
					self.rerollDice(dice, d)


		if msg==True : print(dice)
		final_score, key = score.getMaxScore(dice)
		return [max_score, final_score]

