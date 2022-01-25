"""
File: boggle.py
Name: 賴珈汶
----------------------------------------
TODO:
"""

import time	 # This file allows you to calculate the speed of your algorithm

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: This program plays a game that user needs to input 4X4 letters. It will show all possible words and total
	number of words.
	"""
	####################
	words = read_dictionary()
	total_lst = []
	while True:
		for i in range(4):
			s_i = str(input(f'{i+1} row of letters: '))
			lst = s_i.split()
			total_lst += s_i.split()
			if len(lst) != 4 or len(lst[0]) != 1 or len(lst[1]) != 1 or len(lst[2]) != 1 or len(lst[3]) != 1:
				print(f'Illegal input')
				break
		break
	start = time.time()
	d = {}
	for i in range(len(total_lst)):
		d[i] = total_lst[i]
	x_y_dict = {}
	for index, letter in d.items():
		x_y_dict[(index % 4, index // 4)] = letter
	find_word(x_y_dict, words)
	####################
	end = time.time()
	print(f'The speed of your boggle algorithm: {end - start} seconds.')
	print('----------------------------------')


def find_word(dic, words):
	# double for loop to check 16 letters
	word_lst = []
	for y in range(4):
		for x in range(4):
			find_word_helper(dic, dic[(x, y)], [(x, y)], (x, y), word_lst, words)
	print(f'There are {len(word_lst)} words in total.')


def find_word_helper(dic, current_s, current_lst, current_pos, word_lst, words):
	# print the word which length is more over 4 and exists in the dictionary.txt.
	if len(current_lst) >= 4:
		if current_s in words:
			word_lst.append(current_s)
			print(f'Found: "{current_s}"')
	# double for loop to check 8 neighbors of the letter
	# it can find the more words even if it reaches base case
	for n in range(-1, 2, 1):			# -1, 0, 1
		for m in range(-1, 2, 1):		# -1, 0, 1
			# get neighbor index
			nei_x = current_pos[0] + n
			nei_y = current_pos[1] + m
			if nei_x < 0 or nei_y < 0 or nei_x > 3 or nei_y > 3:  # out of the 4X4 range
				pass
			else:
				if (nei_x, nei_y) in current_lst:		# can not add the position which had been added
					pass
				else:
					# choose
					current_lst.append((nei_x, nei_y))
					current_s += dic[(nei_x, nei_y)]
					# explore
					if current_s not in word_lst:
						if has_prefix(current_s, words):
							find_word_helper(dic, current_s, current_lst, (nei_x, nei_y), word_lst, words)
					# un-choose
					current_lst.pop()
					current_s = current_s[0:len(current_s)-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	words = []
	with open(FILE, 'r') as f:
		for line in f:
			words.append(line.replace('\n', ''))
	return words


def has_prefix(sub_s, words):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param words: (list) All words in dictionary.txt
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	exit_in_dict = 0
	for i in range(len(words)):
		if words[i].startswith(sub_s):
			exit_in_dict += 1
			return True
	if exit_in_dict == 0:
		return False


if __name__ == '__main__':
	main()
