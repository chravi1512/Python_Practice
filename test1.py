a=int(input("enter the number: "))

total  = a+100

print (f"Total is {total}")

print(7%2)


def splitsum(l):
    pos = sum(x**2 for x in l if x > 0)
    neg = sum(abs(x)**3 for x in l if x < 0)
    return [pos, neg]

