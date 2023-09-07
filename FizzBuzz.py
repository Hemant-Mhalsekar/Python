# A program that checks if a number is divisible by both 3 and 5, if true then it prints "FizzBuzz". 
# If the number is divisible by 3 then it prints "Fizz"
# If the number is divisible by 5 then it prints "Buzz"
# Used for loop and if else loop   

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)