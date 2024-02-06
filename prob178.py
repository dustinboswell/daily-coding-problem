'''
This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.
'''
import random

def play_game(final_die, prev_die):
    num_rolls = 0
    prev = None
    while True:
        die = random.randint(1,6)
        num_rolls += 1
        if prev == prev_die and die == final_die:
            return num_rolls
        prev = die

def avg(nums):
    return sum(nums) / len(nums)

game1_nums = [play_game(final_die=6, prev_die=5) for _ in range(300000)]
print(f"Game1(5 then 6): {avg(game1_nums):2.2f} rolls on avg")
game2_nums = [play_game(final_die=5, prev_die=5) for _ in range(300000)]
print(f"Game2(5 then 5): {avg(game2_nums):2.2f} rolls on avg")
