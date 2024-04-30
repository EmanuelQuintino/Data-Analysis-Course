# variables

name1 = "test1"
name2 = "test2"
name2 = name1

name1, name2 = "test1", "test2"
name1, name2 = "test1", "test2"

name1 = name2 = "test1"

print(name1 * 3)
print(name2[::-1])

# primitive types

name = "Emanuel" #string 
age = 30 #int
height = 1.85 #float
is_admin = True #boolean

print(type(name))
print(type(age))
print(type(height))
print(type(is_admin))

name = "Jorge" 
age = 20

name = input("Digite seu nome: ")
age = input(f"Digite sua idade, {name}: ")

print("Sou " + name + " e tenho " + str(age) + " anos")
print(f'Sou {name} tenho {age} anos e {height} de altura')

new_age = float(age)
new_height = int(height)

print(new_age)
print(type(new_age))

print(new_height)
print(type(new_height))

# structural types or collections

list = ["string", 2, True, [2, "três"]]
#           0      1    2         3
#          -4     -3   -2        -1

print(list[0])
print(list[-2])
print(list[-1][1])

list[2] = False
list[-1][0] = "D"

print(list)
print(len(list))

tuple = ("string", 2, True, [2, "Três"])
# tuple = ("cpf", "123.123.123-12", 12312312312)

print(tuple[0])
print(tuple[-2])
print(tuple[3][1])

tuple[2] = False # error: tuple is immutable

print(tuple)
print(len(tuple))

set = {"violão", "guitarra", "bateria"}
set.add("baixo")
set.remove("violão")
set.pop()
print(set)

dict = {
  "name":"Emanuel",
  "age":30,
  "is_admin": False,
  "favorites": ["matrix", "jurassic park", "the terminator"]
}

print(dict["favorites"][1])
print(dict.get("favorites", "Não foi possível recuperar dado")[1])
