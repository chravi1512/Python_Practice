first_name="ravi"
last_name="ch"
print(f"{first_name} {last_name}".upper())
print("No. of Languages:\n\t\tPython\n\t\tJava")


first = "kaleidoscope"
second = ""
for i in range(len(first)-1,-1,-2):
  second = first[i]+second
  print(second)