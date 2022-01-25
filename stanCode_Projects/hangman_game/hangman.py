"""
File: hangman.py
Name: 賴珈汶
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:This program plays hangman game.
    """
    guesses_number = N_TURNS
    s = random_word()
    # print(s)
    l1_s = len(s)
    # print(l1_s)
    bl = blank(l1_s)
    print("The word looks like: " + str(bl))
    print("You have " + str(N_TURNS) + " guesses left.")
    g = str(input("Your guess: "))
    g1 = g.upper()
    l1_g = len(g1)
    # print(l1_g)
    g1 = correct_letter_input(g1, l1_g)
    l1_g = correct_number_input(g1, l1_g)
    # match1(g1, s, guesses_number, bl)
    ans = match1(g1, s, bl)
    guesses_number = match3(g1, s, guesses_number)
    while True:
        g = str(input("Your guess: "))
        g1 = g.upper()
        l1_g = len(g1)
        # print(l1_g)
        g1 = correct_letter_input(g1, l1_g)
        l1_g = correct_number_input(g1, l1_g)
        # match2(g1, s, guesses_number, ans)
        ans = match2(g1, s, guesses_number, ans)
        if ans.find("-") == -1:
            print("You win!!")
            print("The word was: " + str(s))
            break
        guesses_number = match3(g1, s, guesses_number)
        if guesses_number == 0:
            print("There is no " + str(g1) + " 's in the word.")
            print("You are completely hung : (")
            print("The word was: " + str(s))
            break


def match2(g1, s, guesses_number, ans):
    """
    The second and subsequence letters, user inputted, matched with the answer or not.
    """
    answer1 = ""
    if g1 in s:
        print("You are correct!")
        for k in range(len(s)):
            ch3 = s[k]
            ch4 = ans[k]
            if ch3 == g1:
                answer1 += g1
            else:
                answer1 += ch4
        if answer1.find("-") != -1:
            print("The word looks like: " + answer1)
        return answer1
    else:
        ans = ans
        guesses_number -= 1
        if guesses_number == 0:
            pass
        else:
            print("There is no " + str(g1) + "'s in the word.")
            print("The word looks like: " + str(ans))
    return ans


def match1(g1, s, bl):
    """
    The first letter, user inputted, matched with the answer or not.
    """
    ans = ""
    if g1 in s:
        print("You are correct!")
        for j in range(len(s)):
            ch1 = s[j]
            ch2 = bl[j]
            if ch1 == g1:
                ans += g1
            else:
                ans += ch2
        print("The word looks like: " + ans)
        return ans
    else:
        ans = bl
        print("There is no " + str(g1) + "'s in the word.")
        print("The word looks like: " + str(bl))
    return ans


def match3(g1, s, guesses_number):
    """
    Give the guesses_number that the user has.
    """
    if g1 in s:
        print("You have " + str(guesses_number) + " guesses left.")
    else:
        guesses_number = guesses_number - 1
        if guesses_number == 0:
            pass
        else:
            # print("There is no " + str(g1) + "'s in the word.")
            print("You have " + str(guesses_number) + " guesses left.")
    return guesses_number


def correct_number_input(g1, l1_g):
    """
    To make sure the letter, user inputted, is one letter.
    """
    if g1.isalpha():
        if l1_g == 1:
            pass
        else:
            print("illegal format.")
            g = str(input("Your guess: "))
            g1 = g.upper()
            l1_g = len(g1)
        return l1_g
    else:
        print("illegal format.")
        g = str(input("Your guess: "))
        g1 = g.upper()
        l1_g = len(g1)
    return l1_g


def correct_letter_input(g1, l1_g):
    """
    To make sure the user input is letter.
    """
    while True:
        if g1.isalpha():
            if l1_g == 1:
                break
            else:
                print("illegal format.")
                g = str(input("Your guess: "))
                g1 = g.upper()
                l1_g = len(g1)
        else:
            print("illegal format.")
            g = str(input("Your guess: "))
            g1 = g.upper()
            l1_g = len(g1)
    return g1


def blank(l1):
    """
    Display the length of the letters by " - " .
    """
    bl = ""
    for i in range(l1):
        bl = bl + "-"
    return bl


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
