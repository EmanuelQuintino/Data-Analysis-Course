# File Manipulation

import os

file = open("Python/class-07-list.txt", "r+", encoding='utf-8')
file2 = open("Python/class-07-list2.txt", "w", encoding='utf-8')

# "r" - read
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())

list = file.readlines()
print(list)

for i in list:
  print(i.upper())
  file2.write(f"{i.upper()}")

# "a" - append
# "w" - write
# file.write("avião\n")
# file2.write("avião\n")

# file2 = open("Python/class-07-list.txt", "w", encoding='utf-8')
item = "bola"
new_list = []
for i in list:
  if i.strip() != item:
    new_list.append(i)
    file2.write(i)

print(new_list)

file.close()
file2.close()

# os.remove("Python/class-07-list2.txt")
