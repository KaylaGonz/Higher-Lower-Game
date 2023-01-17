import random
from replit import clear
from game_data import data
from art import logo, vs


def random_celeb():
  """Return a random number from 0 to 49"""
  random_num = random.randint(0,49)
  return random_num

def format_data(celeb):
  """Takes selected number and formats data into a printable template"""
  celeb_name = data[celeb]['name']
  celeb_descr = data[celeb]['description']
  celeb_country = data[celeb]['country']
  return f"{celeb_name}, a {celeb_descr}, from {celeb_country}"
  

#higher vs lower function, compares followers
def check_answer(celeb1, celeb2, user_guess):
  """Takes account number and user's guess and returns if the user is right"""
  follower_amount1 = data[celeb1]['follower_count']
  follower_amount2 = data[celeb2]['follower_count']
  if follower_amount1 > follower_amount2:
    correct_answer = "a"
  else: 
    correct_answer = "b"

  if correct_answer == user_guess:
    return True
  else:
    return False


def game():
  print(logo)
  counter = 0
  game_continue = True
  celeb_A = random_celeb()
  
  while game_continue:
    print(f"Compare A: {format_data(celeb_A)}.")
    print(vs)
    celeb_B = random_celeb()
    if celeb_A == celeb_B:
      celeb_B = random_celeb()
      
    print(f"Against B: {format_data(celeb_B)}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(celeb_A, celeb_B, user_choice)

    clear()
    print(logo)
    
    if is_correct:
      counter +=1
      print(f"You're right! Current score: {counter}")
      celeb_A = celeb_B
    else:
      print(f"Sorry, that's wrong. Final score: {counter}")
      game_continue = False

    
game()