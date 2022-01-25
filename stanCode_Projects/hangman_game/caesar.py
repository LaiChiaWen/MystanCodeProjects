"""
File: caesar.py
Name: 賴珈汶
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:This program does decipher.
    """
    m = int(input("Secret number: "))
    s = input("What's the ciphered string? ")
    s1 = s.upper()
    new_alphabet = movement(ALPHABET, m)
    # print(new_alphabet)
    ans = decipher(s1, new_alphabet, m)
    print("The deciphered string is: " + ans)


def movement(ALPHABET, m):
    """
    Change to the new alphabet.
    """
    one_part = ALPHABET[:m]
    # print(one_part)
    two_part = ALPHABET[25 - m + 1:]
    # print(two_part)
    three_part = ALPHABET[m:25 - m + 1]
    # print(three_part)
    new_alphabet = two_part + one_part + three_part
    return new_alphabet


def decipher(s1, new_alphabet, m):
    """
    Decipher the string.
    """
    ans = ""
    for i in range(len(s1)):
        ch = s1[i]
        if ch == 'A':
            if m + new_alphabet.find('A') >= 26:
                n = m + new_alphabet.find('A') - 26
            else:
                n = m + new_alphabet.find('A')
            ans += new_alphabet[n]
        elif ch == 'B':
            if m + new_alphabet.find('B') >= 26:
                n = m + new_alphabet.find('B') - 26
            else:
                n = m + new_alphabet.find('B')
            ans += new_alphabet[n]
        elif ch == 'C':
            if m + new_alphabet.find('C') >= 26:
                n = m + new_alphabet.find('C') - 26
            else:
                n = m + new_alphabet.find('C')
            ans += new_alphabet[n]
        elif ch == 'D':
            if m + new_alphabet.find('D') >= 26:
                n = m + new_alphabet.find('D') - 26
            else:
                n = m + new_alphabet.find('D')
            ans += new_alphabet[n]
        elif ch == 'E':
            if m + new_alphabet.find('E') >= 26:
                n = m + new_alphabet.find('E') - 26
            else:
                n = m + new_alphabet.find('E')
            ans += new_alphabet[n]
        elif ch == 'F':
            if m + new_alphabet.find('F') >= 26:
                n = m + new_alphabet.find('F') - 26
            else:
                n = m + new_alphabet.find('F')
            ans += new_alphabet[n]
        elif ch == 'G':
            if m + new_alphabet.find('G') >= 26:
                n = m + new_alphabet.find('G') - 26
            else:
                n = m + new_alphabet.find('G')
            ans += new_alphabet[n]
        elif ch == 'H':
            if m + new_alphabet.find('H') >= 26:
                n = m + new_alphabet.find('H') - 26
            else:
                n = m + new_alphabet.find('H')
            ans += new_alphabet[n]
        elif ch == 'I':
            if m + new_alphabet.find('I') >= 26:
                n = m + new_alphabet.find('I') - 26
            else:
                n = m + new_alphabet.find('I')
            ans += new_alphabet[n]
        elif ch == 'J':
            if m + new_alphabet.find('J') >= 26:
                n = m + new_alphabet.find('J') - 26
            else:
                n = m + new_alphabet.find('J')
            ans += new_alphabet[n]
        elif ch == 'K':
            if m + new_alphabet.find('K') >= 26:
                n = m + new_alphabet.find('K') - 26
            else:
                n = m + new_alphabet.find('K')
            ans += new_alphabet[n]
        elif ch == 'L':
            if m + new_alphabet.find('L') >= 26:
                n = m + new_alphabet.find('L') - 26
            else:
                n = m + new_alphabet.find('L')
            ans += new_alphabet[n]
        elif ch == 'M':
            if m + new_alphabet.find('M') >= 26:
                n = m + new_alphabet.find('M') - 26
            else:
                n = m + new_alphabet.find('M')
            ans += new_alphabet[n]
        elif ch == 'N':
            if m + new_alphabet.find('N') >= 26:
                n = m + new_alphabet.find('N') - 26
            else:
                n = m + new_alphabet.find('N')
            ans += new_alphabet[n]
        elif ch == 'O':
            if m + new_alphabet.find('O') >= 26:
                n = m + new_alphabet.find('O') - 26
            else:
                n = m + new_alphabet.find('O')
            ans += new_alphabet[n]
        elif ch == 'P':
            if m + new_alphabet.find('P') >= 26:
                n = m + new_alphabet.find('P') - 26
            else:
                n = m + new_alphabet.find('P')
            ans += new_alphabet[n]
        elif ch == 'Q':
            if m + new_alphabet.find('Q') >= 26:
                n = m + new_alphabet.find('Q') - 26
            else:
                n = m + new_alphabet.find('Q')
            ans += new_alphabet[n]
        elif ch == 'R':
            if m + new_alphabet.find('R') >= 26:
                n = m + new_alphabet.find('R') - 26
            else:
                n = m + new_alphabet.find('R')
            ans += new_alphabet[n]
        elif ch == 'S':
            if m + new_alphabet.find('S') >= 26:
                n = m + new_alphabet.find('S') - 26
            else:
                n = m + new_alphabet.find('S')
            ans += new_alphabet[n]
        elif ch == 'T':
            if m + new_alphabet.find('T') >= 26:
                n = m + new_alphabet.find('T') - 26
            else:
                n = m + new_alphabet.find('T')
            ans += new_alphabet[n]
        elif ch == 'U':
            if m + new_alphabet.find('U') >= 26:
                n = m + new_alphabet.find('U') - 26
            else:
                n = m + new_alphabet.find('U')
            ans += new_alphabet[n]
        elif ch == 'V':
            if m + new_alphabet.find('V') >= 26:
                n = m + new_alphabet.find('V') - 26
            else:
                n = m + new_alphabet.find('V')
            ans += new_alphabet[n]
        elif ch == 'W':
            if m + new_alphabet.find('W') >= 26:
                n = m + new_alphabet.find('W') - 26
            else:
                n = m + new_alphabet.find('W')
            ans += new_alphabet[n]
        elif ch == 'X':
            if m + new_alphabet.find('X') >= 26:
                n = m + new_alphabet.find('X') - 26
            else:
                n = m + new_alphabet.find('X')
            ans += new_alphabet[n]
        elif ch == 'Y':
            if m + new_alphabet.find('Y') >= 26:
                n = m + new_alphabet.find('Y') - 26
            else:
                n = m + new_alphabet.find('Y')
            ans += new_alphabet[n]
        elif ch == 'Z':
            if m + new_alphabet.find('Z') >= 26:
                n = m + new_alphabet.find('Z') - 26
            else:
                n = m + new_alphabet.find('Z')
            ans += new_alphabet[n]
        elif ch == ' ':
            ans += " "
        elif ch == '!':
            ans += '!'
        elif ch == '?':
            ans += '?'
        elif ch == ',':
            ans += ','
        elif ch == '.':
            ans += '.'
        elif ch == '(':
            ans += '('
        elif ch == ')':
            ans += ')'
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
