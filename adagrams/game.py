import random

def draw_letters():

	""" 
	This function takes no parameters and returns a pool of 10 random letters, 
	which represents the player's hand. 
	"""
	
	# Initialize available_pool list
	available_pool = []	
	
	# Create dictionary of letter quantities
	letter_quantities = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
	}

	# Add letters to pool based on quantity in dictionary
	for letter in letter_quantities:
		for i in range(letter_quantities[letter]):
			available_pool.append(letter)

	# Sample 10 random letters from pool and return as list
	return random.sample(available_pool, 10)

def uses_available_letters(word, letter_bank):

	"""
	This function takes two parameters, a string 'word' and a list of letters 'letter_bank'.
	Returns True if every letter in 'word' is available in 'letter_bank', otherwise returns False.
	"""

	# Make copy of letter_bank so that original list is not modified
	letter_bank_copy = list(letter_bank)

	# Iterate through each letter in word
	for letter in word.upper():

		# If letter not in letter_bank_copy, return False
		if letter not in letter_bank_copy:
			return False
		
		# Remove letter from letter_bank_copy if it is in the copy
		letter_bank_copy.remove(letter)
	
	# Return True if every letter in word is in letter_bank
	return True


def score_word(word):

	"""
	This function takes one parameter, a string 'word', and returns the score of the word.
	The score of each letter is determined by the score chart given.
	If the word is 7 or more letters long, an additional 8 points are added to the score.
	"""

	# Initialize total score to 0
	total = 0

	# Create dictionary of letter scores
	letter_scores = {
		'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
		'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
		'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
	}

	# Iterate through each letter in word and add corresponding score to total
	for letter in word:
		total += letter_scores[letter.upper()]

	# Add 8 points to score if word is 7 or more letters long
	if len(word) >= 7:
		total += 8
	
	return total

def get_highest_word_score(word_list):

	"""
	Takes a list of words and returns the highest scoring word and its score.
	If there are ties, the function returns the word with the fewest letters, unless the highest-scoring
	word has 10 letters, in which case it is returned regardless of ties.
	"""

	# Initialize empty highest score and highest scoring word
	highest_score = 0
	highest_word = ''
	
	# Iterate through each word in word_list 
	for word in word_list:

		# Score word using the score_word function
		score = score_word(word)

		# If word's score is higher than highest score, set highest_score and highest_word to current
		if score > highest_score:
			highest_score = score
			highest_word = word

		# If there is a tie, determine highest score based on tie-breaker rules
		elif score == highest_score:

			# If highest-scoring word has 10 letters, return it regardless of ties
			if len(highest_word) == 10:
					continue
			
			# If current word has 10 letters, make it the new highest scoring word
			elif len(word) == 10:
					highest_word = word

			# If current word has fewer letters than the current highest scoring word, make it the new highest
			elif len(word) < len(highest_word):
					highest_word = word

	return (highest_word, highest_score)
