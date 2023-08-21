
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

# Write your code below this line 👇
myChoice = " "
print("What do you choose?")
choice = input("Type R for Rock , P for paper or S for Scissors. ")

if choice == "R":
    print(rock)
    myChoice = 0
elif choice == "P":
    print(paper)
    myChoice = 1
elif choice == "S":
    print(scissors)
    myChoice = 2

print(myChoice)

print("Computer chose:")

computerChoice = [rock, paper, scissors]

randomInt = random.randint(0, 2)
print(computerChoice[randomInt])

computerChosen = randomInt
print(computerChosen)

if myChoice == 0:
    if myChoice == computerChosen:
        print("It's draw")
    elif myChoice == 1 and con:
        print("You loose ")
    elif myChoice == 2:
        print("You won")

if myChoice == 1:
    if myChoice == computerChosen:
        print("It's draw")
    elif myChoice == 2:
        print("You loose ")
    elif myChoice == 0:
        print("You won")

if myChoice == 2:
    if myChoice == computerChosen:
        print("It's draw")
    elif myChoice == 2:
        print("You loose ")
    elif myChoice == 1:
        print("You won")
