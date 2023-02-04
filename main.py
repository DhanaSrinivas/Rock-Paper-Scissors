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

options = [rock, paper, scissors]


print("Welcome to Rock Paper Scissors game")

your_choice = int(input("What do you choose ? Type 0 for Rock🪨, 1 for paper📄, 2 for scissors✂️\n"))
print(options[your_choice])

print("Computer chose: ")
computer_choice = random.randint(0, 2)
print(options[computer_choice])

if your_choice == computer_choice:
    print("Game drawn😛")
elif your_choice == 0 and computer_choice == 2:
    print("You won🥳")
elif your_choice == 2 and computer_choice == 0:
    print("You lose😢")
elif your_choice < computer_choice:
    print("You lose😢")
else:
    print("You won🥳")
