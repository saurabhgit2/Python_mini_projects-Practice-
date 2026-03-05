print("Hello, welcome to the Quiz Game")

playing=input("Do you want to play?  ")

if playing.lower()!="yes":
    print("You chose not to proceed. It's okay, be brave next time")
    quit()

score=0
# First Question
answer=input("What is the full form of CPU? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
    print(f"Your score is {score}")
else:
    print("Incorrect!")

# Second Question
answer=input("What is the full form of GPU? ")
if answer.lower()=="graphic processing unit":
    print("Correct!")
    score+=1
    print(f"Your score is {score}")
else:
    print("Incorrect!")

# Third Question
answer=input("What is 2+2? ")
if answer.lower()=="4":
    print("Correct!")
    score+=1
    print(f"Your score is {score}")
else:
    print("Incorrect!")


# Fourth Question
answer=input("What is life? ")
if answer.lower()=="unfair":
    print("Correct!")
    score+=1
    print(f"Your score is {score}")
else:
    print("Incorrect!")

print(f"Your final score is {score}")
