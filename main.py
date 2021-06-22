import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_image =[rock, paper, scissors]

while True:
    player_chose = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
    if player_chose >= 3 or player_chose < 0:
        print("Error! Please input 0, 1, 2 !")
    else:
        print("You have chose:")
        print(game_image[player_chose])
        break

computer_chose = random.randint(0,2)
print("Computer have chose:")
print(game_image[computer_chose])

if player_chose >= 3 or player_chose < 0:
    print("Error! Please input 0, 1, 2")
elif player_chose == 0 and computer_chose == 2:
    print("You Win!")
elif player_chose == 2 and computer_chose == 0:
    print("You Lose!")
elif player_chose > computer_chose:
    print("You Win!")
elif computer_chose > player_chose:
    print("You Lose!")
elif player_chose == computer_chose:
    print("You Draw!")
