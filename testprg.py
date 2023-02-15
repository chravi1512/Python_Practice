##A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.
##
##Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise. (If m is not positive,
##                                                                                                                                                    your function should return False.)

n = int(input("Enter the number : "))

for p in range (1,n+1):
    if p>2<n:
        if (n%p==0):
        
            print(f"{p} is not prime number")
        else:
            print(f"{p} is primenumber")
# for q in range (1,n+1):
#      if q>2:
#          v=(n%q==0)
#          print(f"{q} is not prime number")
