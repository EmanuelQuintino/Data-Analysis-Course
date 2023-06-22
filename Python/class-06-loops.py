# Loops

# i = 1
# while i <= 10:
#   print(i)
#   i += 1

for i in range(5, 11, 2):
  print(i)

# list_names = ["Pedro", "João", "Carla", "Clara"]
# for name in list_names:
  # print(name)

array = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"],
]

for i in array:
  for j in i:
    print(j)