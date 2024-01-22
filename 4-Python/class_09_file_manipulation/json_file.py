import json

data = [
  {"name": "João", "age": 25,},
  {"name": "Maria", "age": 30},
  {"name": "Pedro", "age": 35},
  {"name": "Ana", "age": 28},
]

# for i in data:
#   for k, v in i.items():
#     print(k, v)

# print(json.dumps(data, ensure_ascii=False))

file_path = "3-Python/files/students.json"
with open(file_path, "w", newline="\n", encoding="utf-8") as file:
  writer = file.write(json.dumps(data, ensure_ascii=False))

with open(file_path, "r", encoding="utf-8", newline="\n") as file:
  reader = file.read()
  data = json.loads(reader)
  print(data)

  for i in data:
    print(i["name"])
