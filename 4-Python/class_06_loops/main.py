import time

# loops

# array_numbers = [1, 2, 3, 4, 5]

start_time = time.time()

i = 1
# while i <= 10000:
#   print(i)
#   i += 1

end_time = time.time()
print(end_time - start_time)

# i = 0
# while i < 5:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 0
# while i <= len(array_numbers):
#   print(array_numbers[i])
#   i += 1

for i in range(1, 10, 2):
  print(i)

# for i in array_numbers:
#   print(i)

# name = "Emanuel"
# for i in name:
#   print(i)

# list_names = ["Pedro", "João", "Carla", "Clara"]

# for name in list_names:
#   print(name)

# array = [
#   ["A", "B", "C"],
#   ["D", "E", "F"],
#   ["G", "H", "I"],
# ]

# for i in array:
#   for j in i:
#     print(j)

list_users = [
  {"name":"Carla", "age": 14},
  {"name":"Pedro", "age": 22},
  {"name":"João", "age": 25},
  {"name":"Clara", "age": 18},
]

# for user in list_users:
#   if user["age"] > 20:
#     print(f"{user['name']} tem {user['age']} anos")

# for user in list_users:
#   if user["name"] == "Carla":
#     print(f"{user['name']} tem {user['age']} anos")
#     break
#   print("-")

# for user in list_users:
#   for k, v in user.items():
#     print(v)
