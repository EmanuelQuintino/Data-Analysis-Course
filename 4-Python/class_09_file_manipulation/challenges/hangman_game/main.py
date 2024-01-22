from hangman_draw import hangman_drawings 
from os import name, system 
import random

def clear_screen():
  if name == "nt":
    system("cls")
  else:
    system("clear")

with open("3-Python/challenges/hangman_game/word_list.txt", "r", encoding="utf-8") as file:
  list = file.readlines()
  words = [i.strip() for i in list]
  print(words)
  word = random.choice(words)
  hide_word = ["_" for i in word]
  letters = []
  chances = 6

  while True:
    print("Bem-vindo ao jogo da forca!")
    print(hangman_drawings[::-1][chances])
    print("\b")
    print(f"Chances restantes: {chances}")
    print(f"Letras citadas: {' '.join(letters)}")
    print("Adivinha a palavra abaixo:")
    print("\b")
    print(' '.join(hide_word))
    print("\b")

    if "_" not in hide_word:
      print("\bVocê venceu!")
      break

    if chances == 0:
      print(f'\bVocê perdeu! A palavra era "{word.capitalize()}".')
      break

    letter = input("Informe uma letra: ").lower()
    if letter == "" or letter.isnumeric() or letter in letters:
      clear_screen()
      continue

    if letter in word.lower():
      for k, i in enumerate(word):
        if letter == i:
          hide_word[k] = letter
    else:
      chances -= 1
    
    letters.append(letter)

    clear_screen()
