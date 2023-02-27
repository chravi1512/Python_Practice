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
