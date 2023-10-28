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

#Write your code below this line 👇
import random
user_choice = input("Choose 1 rock, 2 paper, 3 scissors: ")
user_choice = int(user_choice)
computer_choice = random.randint(1,3)

if user_choice == 1:
  print(rock)
elif user_choice == 2:
  print(paper)
elif user_choice == 3:
  print(scissors)

print("Computer chose:")
if computer_choice == 1:
  print(rock)
elif computer_choice == 2:
  print(paper)
elif computer_choice == 3:
  print(scissors)

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 1 and computer_choice == 3:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 2 and computer_choice == 3:    
    print("You lose")
elif user_choice == 3 and computer_choice == 1:
    print("You lose")
elif user_choice == 3 and computer_choice == 2:
    print("You win")
else:
    print("Invalid input")

