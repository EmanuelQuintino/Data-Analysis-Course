with open("4-Python/class_09_file_manipulation/files/films.txt", "r", encoding="utf-8") as films, \
     open("4-Python/class_09_file_manipulation/files/file.txt", "w", encoding="utf-8") as file:

  for film in films:
    file.write(film.upper())
