from myFunctions import *


# worst case 10000 times
iterations = 10000
attempts = 0
highest_attempt = 0
lowest_attempt = 1000

options = all_1000_options()

for x in range(iterations):
    three_random_numbers = get_three_random_numbers()
    iteration = worst_case_algorithm(options, three_random_numbers)
    attempts += iteration
    highest_attempt = iteration if iteration > highest_attempt else highest_attempt
    lowest_attempt = iteration if iteration < lowest_attempt else lowest_attempt

print(f"Number of Tries: {iterations}\n"
      f"Highest number of guess in a try: {highest_attempt}\n"
      f"Lowest tries: {lowest_attempt}\n"
      f"Number of Correct tries: {iterations}\n"
      f"Average number of tries: {attempts}/{iterations}: {attempts/iterations} ")


#  Guessing Game - algorithm is user inputted guesses
# three_random_numbers = get_three_random_numbers()
# print(three_random_numbers)
# user_guesses = get_user_guesses()
# print(check_for_win(user_guesses, three_random_numbers))
