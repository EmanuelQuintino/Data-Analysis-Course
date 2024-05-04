# enumerate

array = ["A", "B", "C"]

print(list(enumerate(array)))

for i, v in enumerate(array):
  print(i, v) 

for i, v in enumerate(range(10)):
  print(i, v) 
