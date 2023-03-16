import random

def draw_letters():
	available_pool = []	
	letter_quantities = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
	}
	for letter in letter_quantities:
		for i in range(letter_quantities[letter]):
			available_pool.append(letter)

	return random.sample(available_pool, 10)

def uses_available_letters(word, letter_bank):
	letter_bank_copy = list(letter_bank)
	for letter in word.upper():
		if letter not in letter_bank_copy:
			return False
		letter_bank_copy.remove(letter)
	return True


def score_word(word):
	total = 0
	letter_scores = {
		'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
		'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
		'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
	}
	for letter in word:
		total += letter_scores[letter.upper()]

	if len(word) >= 7:
		total += 8
	
	return total

def get_highest_word_score(word_list):
	pass
