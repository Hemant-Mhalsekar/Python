print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? (yes/no): ")

if playing != "yes":
    quit()

print("Let's begin!")

# Question 1
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct answer")
else:
    print("Wrong answer. The correct answer is central processing unit.")

