# File Manipulation

import os

file = open("Python/class-07-list.txt", "r", encoding='utf-8')
file2 = open("Python/class-07-list2.txt", "w", encoding='utf-8')

# "r" - read
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.read())

list = file.readlines()
# print(list[2])

# "a" - append
# "w" - write
# file.write("avião\n")
# file2.write("avião\n")

# for i in list:
#   file2.write(f"{i.upper()}")
#   # print(i.upper())

item = "bola"
new_list = []
for i in list:
  if i.strip() != item:
    new_list.append(i)
    file2.write(i)

print(new_list)

file.close()
file2.close()

os.remove("Python/class-07-list2.txt")
