import csv

data = [
  ["Name", "Age", "City"],
  ["João", 25, "São Paulo"],
  ["Maria", 30, "Rio de Janeiro"],
  ["Pedro", 35, "Belo Horizonte"],
  ["Ana", 28, "Brasília"],
]

file_path = "4-Python/class_09_file_manipulation/files/students.csv"
with open(file_path, "w", newline="\n", encoding="utf-8") as file:
  writer = csv.writer(file)
  for row in data:
    writer.writerow(row)

with open(file_path, "r", encoding="utf-8", newline="\n") as file:
  reader = csv.reader(file)
  data = list(reader)
  print(data)

  for i in data[1:]:
    print(i)
