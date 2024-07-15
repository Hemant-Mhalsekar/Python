# Python mini project 1
# Quiz Game
# This quiz game asks 4 questions and increments the score pointer by 1.
# Also prints the percentage of correct answers

print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Let's begin!")
score = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer. The correct answer is central processing unit.")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer. The correct answer is graphics processing unit.")
    

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer. The correct answer is random access memory.")
    
    
# Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct answer")
    score += 1
else:
    print("Wrong answer. The correct answer is power supply unit.")

print("You got " + str(score) + " points")
print("You got " + str((score / 4) * 100) + "%")