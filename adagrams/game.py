import random
from .game_constants import *

def draw_letters():
	""" 
	Takes no parameters and returns a pool of 10 random letters, which 
    represents the player's hand. 
	
	Parameters:
        None
	
	Returns:
        list: A list of 10 random letters representing a player's hand.
	"""
	available_pool = [letter for letter, freq in letter_counts.items() \
		for i in range(freq)]

	return random.sample(available_pool, 10)

def uses_available_letters(word, letter_bank):
    """
    Checks if the input word can be made from the input letters (letter_bank).

    Parameters:
        word (str): The string to check against the letter bank.
	
        letter_bank (list): A list of letters as strings that represents the 
        player's hand.

    Returns:
        bool: True if every letter in 'word' is available in 'letter_bank', 
        otherwise False.
    """
    return all(word.upper().count(letter) <= letter_bank.count(letter) 
        for letter in set(word))


def score_word(word):
    """
    This function calculates the score of the input word according to the 
    given score chart. If the word contains 7 or more letters, an additional 
    8 points are added to the score.

    Parameters:
        word (str): A string representing the word whose score is to be 
        calculated.

    Returns:
        int: The score of the given word.
    """
    return sum(letter_scores[letter.upper()] for letter in word) \
        + (8 if len(word) >= 7 else 0)
	
def get_highest_word_score(word_list):
    """
    Takes a list of words and returns the highest scoring word and its score.
    If there are ties, the function returns the word with the fewest letters, 
    unless the highest-scoring word has 10 letters, in which case it is 
    returned regardless of ties.
    Parameters:
        list: A string representing the word whose score is to be 
        calculated.

    Returns:
        tuple: A tuple containing the highest scoring word and its score.
    """
    word_scores = [(word, score_word(word)) for word in word_list]

    max_score = max(word_scores, key=lambda x: x[1])[1]
    max_score_words = [word for word, score in word_scores \
        if score == max_score]

    highest_word = tie_breaker(max_score_words) if len(max_score_words) > 1 \
        else max_score_words[0]
    
    return highest_word, max_score


def tie_breaker(tied_words):
    if any(len(word) == 10 for word in tied_words):
        return next(word for word in tied_words if len(word) == 10)

    highest_word = min(tied_words, key=len)

    return highest_word
