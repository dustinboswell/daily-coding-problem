'''
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''
import random

def shuffle(cards):
    for i in range(len(cards)):
        j = random.randint(i, len(cards)-1)
        tmp = cards[i]
        cards[i] = cards[j]
        cards[j] = tmp
