import os

# "x"  - create
# "r"  - read
# "w"  - write
# "r+" - create
# "a"  - append

path_file_films = "4-Python/class_09_file_manipulation/files/films.txt"

try:
  file = open(path_file_films, "r")
  content = file.read()
  file.close()
except FileNotFoundError:
  print("arquivo não encontrado!")

try:
  with open(path_file_films, "r+", encoding='utf-8') as films:
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
      
except FileNotFoundError:
  print("O arquivo não encontrado!")
    
os.remove(path_file_films)
