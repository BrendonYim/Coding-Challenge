#!/usr/bin/python

import sys
import math

# this calculates the number of permutations depending on the input given
def calcPermutations(w, u):
    # calculating permutation with repeats.
    # equation = N! / (A!*B!*C*...), where in equals number of letters in words and A, B, C... 
    # is the number of repeats for each letter

    # top of equation
    top = math.factorial(len(w))

    # bottom of equation
    bottom = 1
    for letter in u:
        bottom *= math.factorial(letters[letter])

    # return number of permutations possible with letters given
    return top/bottom



# read in command line argument
word = sys.argv[1].upper()


# letters is a dictionary for each letter in alphabet used to quickly lookup how many repeats there are for each letter.
# uniqueLetters contains the all the unique letters in the inputted word/
letters = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
uniqueLetters = []

# finding unique letters
for letter in word:
    if letter not in uniqueLetters:
        uniqueLetters.append(letter)

# finding how many of each letter is in word that was inputted
for letter in word:
    letters[letter] += 1

# now sort letters in uniqueLetters in alphabetical order
uniqueLetters.sort()

# code below finds how many words came before the one that was inputted
i = 0
j = 0
total = 0
while j < len(word):
    i = 0
    x = 0
    while x < j:
        letters[word[x]] -= 1
        x += 1

    while (uniqueLetters[i] is not word[j]) and (i < len(uniqueLetters)):
        if letters[uniqueLetters[i]] > 0:
            letters[uniqueLetters[i]] -= 1
            total += calcPermutations(word[(j+1):], uniqueLetters)

            if letters[uniqueLetters[i]] >= 0:
                letters[uniqueLetters[i]] += 1
        
        i+=1

    x = 0
    while x < j:
        letters[word[x]] += 1
        x += 1

    j += 1

# we have to add one to the total bc total is only the number of words that came
# before our word. the rank of our word is one after that.
print word, 'Rank:', total+1