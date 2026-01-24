import random
rock = '''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ '''

scissors = ''' _       ,'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\. '''

paper = '''          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'  '''

choice = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print(choice[user_choice])
print(f"Computer chose:\n{choice[computer_choice]}")
if user_choice == computer_choice:
    print("It's a draw.")
elif choice[user_choice] == rock:
    if choice[computer_choice] == scissors:
        print("you win.")
    else:
        print("You lose.")
elif choice[user_choice] == scissors:
    if choice[computer_choice] == paper:
        print("you win.")
    else:
        print("You lose.")
else:
    if choice[computer_choice] == rock:
        print("you win.")
    else:
        print("You lose.")

