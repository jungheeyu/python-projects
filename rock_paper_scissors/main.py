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

dic = {0: rock, 1: paper, 2: scissors}
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
bot = random.randint(0,2)

print("user chose: \n" + dic[user])
print("computer chose: \n" + dic[bot])

if user - bot == 1 or bot - user == 2:
  print("You Win!!")
elif user == bot:
  print("Draw!")
else:
  print("You lose!")
