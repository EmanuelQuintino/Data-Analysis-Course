# Crie um lógica que receba o nome e idade do usuário
# Coloque em estrutura de dicionário ("{}"), 
# Adicione ("append") em um array e imprima os usuários

users = [
  {"name": "user1", "age": 20},
  {"name": "user2", "age": 30},
]

name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

user = {
  "name": name,
  "age": age,
}

users.append(user)

for v in users:
  print(v["name"])