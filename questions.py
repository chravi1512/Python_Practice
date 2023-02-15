first = "kaleidoscope"
second = ""
for i in range(len(first)-1,-1,-2):
  second = first[i]+second
  print(second)
