# File Manipulation

# "r" - read
# "w" - write
# "a" - append

file = open("3-Python/files/object_list.txt", "r", encoding='utf-8')
# file2 = open("3-Python/files/object_list2.txt", "w", encoding='utf-8')
# file2 = open("3-Python/files/object_list2.txt", "a", encoding='utf-8')

with open("3-Python/files/object_list.txt", "r", encoding='utf-8') as file:
  print(file.read())

# print(file.read())
# print(file.tell())
# print(file.readline())

# file.seek(0)
# list = file.readlines()
# print(list)

# for i in list:
#   print(i.upper())
#   file2.write(f"{i.upper()}")

# file.write("avião\n")
# file2.write("avião\n")
# file2.write("bola\n")

# # file2 = open("3-Python/files/object_list.txt", "w", encoding='utf-8')
# item = "bola"
# new_list = []
# for i in list:
#   if i.strip() != item:
#     new_list.append(i)
#     file2.write(i)

# print(new_list)

# file.close()
# file2.close()

import os
# os.remove("3-Python/files/object_list2.txt")

# Exercise
# employees = open("3-Python/files/employee_salaries.csv", "r", encoding='utf-8')

# dataset = employees.read()

# print(dataset)

# rows = dataset.split("\n")
# print(rows)

# arrayEmployees = []

# for row in rows:
  # split_row = row.split(",")
  # arrayEmployees.append(split_row)

# print(arrayEmployees)
# print(len(arrayEmployees))
# print(len(arrayEmployees[0]))

# employees.close()

# import pandas as pd

# employees = "3-Python/files/employee_salaries.csv"
# dataset = pd.read_csv(employees)

# print(dataset)
# print(dataset.info())