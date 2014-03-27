Assuming python is installed on the machine, simply move into this folder
with the Terminal/Command Line and run a command similar to the following:

python CodingChallenge.py question

The will take in "question" as a command line argument, find its rank, and
print the word and its rank on the following line.

The code after about line 50 is hard to explain using only words, so I've
included the image "visual.png" to explain my approach a little bit.




The Challenge
Consider a "word" as any sequence of capital letters A-Z (not limited to just
"dictionary words"). For any word with at least two different letters, there 
are other words composed of the same letters but in a different order (for 
instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words; 
for our purposes "AAIILNORSTTY" is also a "word" composed of the same letters 
as these two). 

We can then assign a number to every word, based on where it falls in an 
alphabetically sorted list of all words made up of the same set of letters. One
way to do this would be to generate the entire list of words and find the 
desired one, but this would be slow if the word is long. 

Write a program which takes a word as a command line argument and prints to 
standard output its number. Do not use the method above of generating the 
entire list. Your program should be able to accept any word 25 letters or less 
in length (possibly with some letters repeated), and should use no more than 
1 GB of memory and take no more than 500 milliseconds to run.

Sample words, with their rank:

ABAB = 2 

AAAB = 1

BAAA = 4

QUESTION = 24572 

BOOKKEEPER = 10743