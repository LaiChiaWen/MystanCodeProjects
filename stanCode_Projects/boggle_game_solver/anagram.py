"""
File: anagram.py
Name: 賴珈汶
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
words = []                    # Contains all words in the dictionary.txt


def main():
    """
    TODO:This program finds out the anagrams of the word which is user inputted.
    """
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        s = str(input(f'Find anagrams for: '))
        if s == str(EXIT):
            break
        else:
            start = time.time()
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    read the dictionary.txt and put all words into words(dict).
    """
    with open(FILE, 'r') as f:
        for line in f:
            words.append(line.replace('\n', ''))


def find_anagrams(s):
    """
    :param s: str, the word the user inputs
    :return: print anagrams out
    """
    total_lst = []
    d = {}
    #   Store the string in {index:'letter'}
    for i in range(len(s)):
        d[i] = s[i]
    print(f'Searching...')
    find_anagrams_helper(d, "", [], len(s), total_lst)
    print(f'{len(total_lst)} anagrams: {total_lst}')


def find_anagrams_helper(d, current_s, current_lst, full_len, total_lst):
    if len(current_lst) == full_len:
        if current_s in words:
            total_lst.append(current_s)
            print(f'Found: {current_s}')
            print(f'Searching...')
    else:
        for index, letter in d.items():
            if index in current_lst:
                pass
            else:
                # choose
                current_lst.append(index)
                current_s += letter
                # explore
                if current_s not in total_lst:
                    if has_prefix(current_s):
                        find_anagrams_helper(d, current_s, current_lst, full_len, total_lst)
                # un-choose
                current_lst.pop()
                current_s = current_s[0:len(current_s)-1]   # The lower region doesn't include


def has_prefix(sub_s):
    """
    :param sub_s: str
    :return: boolean, The outcome of True or False that the sub_s in dictionary
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
