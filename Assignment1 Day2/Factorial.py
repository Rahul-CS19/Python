# Phython program to find the factorial of a number

# To take input from user
num = int(input("Enter a number: "))

# check if the number is negative, positive or zero
factorial = 1
if num < 0:
    print("Sorry, factorial does not exit for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
         factorial = factorial * i
    print("The factorial of", num, "is: ", factorial)
