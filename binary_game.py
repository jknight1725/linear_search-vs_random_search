from myFunctions import *

# Binary Search Guessing Game
guesses = 1
lower_bound = 0
upper_bound = 1000

cpu_guess = mid(lower_bound, upper_bound)
computer_says(cpu_guess)
adjustment = get_adjustment()

while adjustment != 'c':
    lower_bound, upper_bound = make_adjustment(adjustment, cpu_guess, lower_bound, upper_bound)
    cpu_guess = mid(lower_bound, upper_bound)
    guesses += 1
    computer_says(cpu_guess)
    adjustment = get_adjustment()
found(cpu_guess, guesses)

