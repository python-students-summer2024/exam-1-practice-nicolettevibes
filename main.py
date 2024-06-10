"""
The code in this file is given to you.
Run this file to call the functions in solutions.py in a way that makes sense.
Feel free to comment out any of it in order to focus only on the functions you are currently working on.
"""

from problem_set_1 import *
from problem_set_2 import *
from problem_set_3 import *

def main():
  """
  Place code within this main function to call whichever functions you want 
  to try out from the other files where you have written code.
  """

  # for example... the following line will call the bark() function in problem_set_1 whenever this main.py file is run.
  bark()
  bark_with_validation()
  respond_to_anything()
  respond_to_anything_but_nonsense()
  weather_helper()

  min_value = 1
  max_value = 100
  random_number = get_random_int(min_value, max_value)
  print(f"Random number between {min_value} and {max_value}: {random_number}")

  max_value_for_guess = 5
  guess_result = get_guess(max_value_for_guess)
  print(f"Guess result for max value {max_value_for_guess}: {'Correct' if guess_result else 'Incorrect'}")

  play_game()

# call the main function
main()
