import csv

dados = [
    ['Name', 'Age', 'City'],
    ['João', 25, 'São Paulo'],
    ['Maria', 30, 'Rio de Janeiro'],
    ['Pedro', 35, 'Belo Horizonte'],
    ['Ana', 28, 'Brasília']
]

file = '3-Python/files/studants.csv'
with open(file, 'w', newline='\n', encoding='utf-8') as file_csv:
  writer = csv.writer(file_csv)
  for linha in dados:
    writer.writerow(linha)

with open("3-Python/files/studants.csv", "r", encoding='utf-8', newline="\n") as file_csv:
  reader = csv.reader(file_csv)
  data = list(reader)
  print(data)

  for i in data[1:]:
    print(i)
