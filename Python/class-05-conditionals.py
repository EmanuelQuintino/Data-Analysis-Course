has_cnh = False

if has_cnh:
  print("Você pode dirigir")
else:
  print("Você não pode dirigir")


# age = int(input("Digite sua idade: "))

# if age < 16:
#   print("Não pode votar")
# elif age >= 16 and age < 18 or age > 70:
#   print("Voto facultativo")
# elif age >= 18 and age <= 70:
#   print("Voto obrigatório")


# Challenge Average
# Sabendo que a média do colégio é 7, crie um programa que receba as notas do aluno e verifique se foi aprovado ou reprovado. Imprima a média e a situação dele:

grade1 = float(input("Digite a primeira nota 1: "))
grade2 = float(input("Digite a primeira nota 2: "))

avg = (grade1 + grade2) / 2

if avg >= 7:
  print(f"Aluno aprovado com média {avg}")
else:
  print(f"Aluno reprovado com média {avg:.2f}")
