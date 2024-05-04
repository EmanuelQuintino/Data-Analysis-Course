# Abra o arquivo de filmes e crie um array
# Passe os nomes do array para caixa alta
# Escreva (write) os nomes em um novo arquivo

path_file_films = "4-Python/class_09_files/files/films.txt"
path_file_upper_films = "4-Python/class_09_files/files/upper_films.txt"

try:
  with open(path_file_films, "r", encoding="utf-8") as films, \
       open(path_file_upper_films, "w", encoding="utf-8") as upper_films:

    for film in films:
      upper_films.write(film.upper())

except FileNotFoundError:
  print("arquivo não encontrado!")
  