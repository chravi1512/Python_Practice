##1. Display three strings ‘Name’,’Is’ ,’James’ as ‘ Name**Is**James’.
a, b, c = 'Name', 'Is', 'James'
print(a, b, c, sep='**')

##2. Accept two numbers input from user, and do mathematical operations, (addition, subtraction, multiplication, division, modulo division, floor division).
a = int(input("Enter value1: "))
b = int(input("Enter value2: "))
print("Addition of 2 numbers is : ",a+b)
print("Subtraction of 2 numbers is : ",a-b)
print("Multpltiplication of 2 numbers is : ",a*b)
print("Division of 2 numbers is : ",a/b)
print("Modulo division of 2 numbers is : ",a%b)
print("Floor division of 2 numbers is : ",a//b)

##3. Convert decimal number into octal number using , format specifier in print function.

a = 10
print("",oct(a))
print("%o"%a)


##4. Display float number with two decimal places, using print function.
b =5.776
print("%.2f"%b)

##5. Take three different strings from input and assign to three different variables and display on the console.

a = input("enter value1: ")
b = input("enter value2: ")
c = input("enter value3: ")
print(f"{a},{b},{c} are good friends")

##6. Take a input string and convert each character into upper case.
a = input("enter the value: ")
print(a.upper())

##7. Take input string and calculate its length without using len function.
a  =input("enter the value: ")
for i in a:
    print(i)
