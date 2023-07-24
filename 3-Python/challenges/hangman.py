from os import name, system 
import random

def clear_screen():
  if name == "nt":
    system("cls")
  else:
    system("clear")

words= ["banana", "maçã"]
word = random.choice(words)
hide_word = ["_" for i in word]
letters = []
chances = 6

while True:
  print("Bem-vindo ao jogo da forca!")
  print("\b")
  print("Adivinha a palavra abaixo:")
  print("\b")
  print(' '.join(hide_word))
  print("\b")
  print("\b")
  print(f"Chances restantes: {chances}")
  print(f"Letras citadas: {' '.join(letters)}")
  print("\b")

  if "_" not in hide_word:
    print("\bVocê venceu!")
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

  if chances == 0:
    print("\bVocê perdeu!")
    break

  clear_screen()
