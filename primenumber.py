# get input from user
num = int(input("Enter a number: "))

# check if number is prime
if num > 1:
    # loop through all numbers from 2 to num-1
    for i in range(2, num):
        # check if num is divisible by i
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

