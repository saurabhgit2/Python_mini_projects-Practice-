# Creating a Rock paper scissor game using Python
# importing random package
import random

# options for game
options=["Rock","Paper","Scissor"]

while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit the game ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    # rock:0 paper:1 scissor:2

print("GoodBye!")
