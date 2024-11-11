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


while True:
    options = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissor.\n"))
    print(options[user_choice])
    computer_choice =  random.randint(0, 2)
    print("computer choice ",computer_choice)
    print(options[computer_choice])

    if user_choice == 0 and computer_choice == 0:
        print("It's a draw!")
    if user_choice == 1 and computer_choice == 1:
        print("It's a draw!")
    if user_choice == 1 and computer_choice == 1:
        print("It's a draw!")
    if user_choice == 0 and computer_choice == 1:
        print("You lose!")
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    if user_choice == 1 and computer_choice == 0:
        print("You win!")
    if user_choice == 1 and computer_choice == 2:
        print("You lose!")
    if user_choice == 2 and computer_choice == 0:
        print("You lose!")
    if user_choice == 2 and computer_choice == 1:
        print("You win!")
    query = input("Press y to play again, q to exit: ").lower()
    if query == 'q':
        break
    