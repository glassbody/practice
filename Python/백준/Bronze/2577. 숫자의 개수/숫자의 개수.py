a = int(input())
b = int(input())
c = int(input())
abc = a * b * c
abc = str(abc)

for x in range(10):
  print(abc.count(str(x)))