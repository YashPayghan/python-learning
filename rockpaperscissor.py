import random
import time
you=input(print("what you choose?\nTYPE 0 for Rock\n TYPE 1 for Paper \n TYPE 2 for Scissors"))
if you=="0":
    print('''You Choose Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
elif you=="1":
    print('''You Choose Paper
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''')
else:
    print('''You Choose Scissors
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

rock = '''
System choose ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
System choose PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
System choose SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices=random.randrange(1,4)
time.sleep(1)
if choices == 1:
    print(rock)
    if you=="0":
        print("match draw")
    elif you=="1":
        print("you win")
    elif you=="2":
        print("you lose")

elif choices == 2:
    print(paper)
    if you=="0":
        print("you lose")
    elif you=="1":
        print("match draw")
    elif you=="2":
        print("you win")
else:
    print(scissors)
    if you=="0":
        print("you win")
    elif you=="1":
        print("you lose")
    elif you=="2":
        print("match draw ")