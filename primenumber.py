n = 3

for p in range (2,n+1):
    if p%2!=0:
        output=n//p
        if output==1 or output==n:
            print(f"{n} is prime number")
            break
    else:
        print(f"{n} is not prime number")
        break
        