import os

os.remove("4-Python/class_09_file_manipulation/files/file.txt")

# "x" - create
# "r" - read
# "w" - write
# "r+" - create
# "a" - append

try:
  file = open("file.txt", "r")
  content = file.read()
  file.close()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

with open("4-Python/class_09_file_manipulation/files/films.txt", "r+", encoding='utf-8') as films:
  print(films.read())
  print(films.tell())

  films.write("Transformers\n")
  films.seek(0)
  print(films.read())
  
  films.seek(0)
  print(films.readline(6))

  films.seek(0)
  list_films = films.readlines()

  for film in list_films:
    print(film.upper())
    