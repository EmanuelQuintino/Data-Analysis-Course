# Abra o arquivo de filmes e crie um array
# Passe os nomes do array para caixa alta
# Escreva (write) os nomes em um novo arquivo

try:
  with open("4-Python/class_09_files/files/films.txt", "r", encoding="utf-8") as films, \
       open("4-Python/class_09_files/files/upper_films.txt", "w", encoding="utf-8") as upper_films:

    for film in films:
      upper_films.write(film.upper())

except FileNotFoundError:
  print("arquivo não encontrado!")
  