# Primitive Types

name = "Emanuel" #string 
age = 30 #int
height = 1.85 #float
is_admin = True #boolean

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_admin))

# name = "Jorge" 
# age = 20

# name = input("Digite seu nome: ")
# age = input(f"Digite sua idade, {name}: ")

# print("Sou " + name + " e tenho " + str(age) + " anos")
# print(f'Sou {name} tenho {age} anos e {height} de altura')

# new_age = float(age)
# new_height = int(height)

# print(new_age)
# print(type(new_age))

# print(new_height)
# print(type(new_height))


# Collections 

list = ["string", 2, True, [2, "Três"]]
#           0      1    2         3

# print(list[0])
# print(list[-2])
# print(list[3][1])

list[2] = False

# print(list)
# print(len(list))


tuple = ("string", 2, True, [2, "Três"])
# tuple = ("cpf", "123.123.123-12", 12312312312)

# print(tuple[0])
# print(tuple[-2])
# print(tuple[3][1])

# tuple[2] = False

# print(tuple)
# print(len(tuple))


set = {"Violão", "Guitarra", "Bateria"}
set.add("Baixo")
# set.remove("Violão")
set.pop()
# print(set)


dict = {
  "name":"Emanuel",
  "age":30,
  "is_admin": False,
  "favorites": ["Matrix", "Jurassic Park", "The Terminator"]
}

# print(dict["favorites"][1])
print(dict.get("favorites", "Não foi possível recuperar dado")[1])
