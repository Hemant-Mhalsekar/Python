print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Let's begin!")

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct answer")
else:
    print("Wrong answer. The correct answer is central processing unit.")

# Question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer")
else:
    print("Wrong answer. The correct answer is graphics processing unit.")
    

# Question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct answer")
else:
    print("Wrong answer. The correct answer is random access memory.")
    
    
# Question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct answer")
else:
    print("Wrong answer. The correct answer is power supply unit.")