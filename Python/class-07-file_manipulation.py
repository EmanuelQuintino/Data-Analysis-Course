# File Manipulation

import os

file = open("Python/files/object_list.txt", "r", encoding='utf-8')
file2 = open("Python/files/object_list2.txt", "w", encoding='utf-8')

# "r" - read
print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())

file.seek(0)
list = file.readlines()
print(list)

# for i in list:
#   print(i.upper())
#   file2.write(f"{i.upper()}")

# # "a" - append
# # "w" - write
# # file.write("avião\n")
# # file2.write("avião\n")

# # file2 = open("Python/files/object_list.txt", "w", encoding='utf-8')
# item = "bola"
# new_list = []
# for i in list:
#   if i.strip() != item:
#     new_list.append(i)
#     file2.write(i)

# print(new_list)

file.close()
file2.close()

os.remove("Python/files/object_list2.txt")
