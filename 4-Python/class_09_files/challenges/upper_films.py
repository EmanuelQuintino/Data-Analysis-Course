# Abra o arquivo de filmes e crie um array
# Passe os nomes do array para caixa alta
# Escreva (write) os nomes em um novo arquivo

try:
  with open("4-Python/class_09_file_manipulation/files/films.txt", "r", encoding="utf-8") as films, \
     open("4-Python/class_09_file_manipulation/files/file.txt", "w", encoding="utf-8") as file:

    for film in films:
      file.write(film.upper())
except FileNotFoundError:
  print("arquivo não encontrado!")
  