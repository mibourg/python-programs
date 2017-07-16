from itertools import chain, combinations

def create_word_list():
	"""Creates a list of almost all words in the English language"""

	#Opens a text file called words.txt and reads it, splits it by line, and creates a list 'words' that contains every word
	with open("words.txt") as f:
		words = f.read().splitlines()
	return words

def find_combinations(letters):
	"""Function to create a list of all letter combinations of a given string"""

	#Uses itertools 'chain' and 'combinations' to accomplish this. Creates lists of sets of all different combinations at different lengths
	#Example: 'abcd' --> [('a',), ('b',), ('c',), ('d',)] --- [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')] ... etc.
	#Then, uses itertools' chain function to create a single sequence out of these multiple sequences
	letters = list(letters)
	return chain.from_iterable(combinations(letters, num) for num in range(1, len(letters)+1))

def find_words(letters):
	"""Given a string, find all possible words within that string"""

	#Creates a list of combinations using the find_combinations() function, mapping it and making a list out of the combinations. 
	#Creates a list of words using create_word_list(). Creates an empty list 'anagrams'.
	combinations = list(map(''.join, find_combinations(letters)))
	words = create_word_list()
	anagrams = list() 

	#For every combination (string) in our list of combinations, make a list out of the combinations. Then, sort the list.
	for combination in combinations:
		combination = list(combination)
		combination.sort()

		#Take every word in the dictionary and check if it is the same length as the combination AND is not already in the 'anagrams' list (to avoid duplicates). 
		#If these conditions are met, make a list out of the word, and sort it.
		#Check if the sorted combination and the sorted word are the same. If so, add the word to the anagrams list. If not, continue looping.
		for word in words:
			if len(word) == len(combination) and word not in anagrams:
				word_as_list = list(word)
				word_as_list.sort()

				if word_as_list == combination:
					anagrams.append(word)

	return anagrams
