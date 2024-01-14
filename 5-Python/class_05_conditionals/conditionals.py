# Conditionals

age = 18
# age = int(input("Digite sua idade: "))

has_cnh = True

if age >= 18 and has_cnh:
  print("Você pode dirigir")
else:
  print("Você não pode dirigir")

# if age < 16:
#   print("Não pode votar")
# elif age >= 16 and age < 18 or age > 70:
#   print("Voto facultativo")
# elif age >= 18 and age <= 70:
#   print("Voto obrigatório")

# try:
#   num1 = float(input("Número 1: "))
#   num2 = float(input("Número 2: "))
#   print(num1/num2)
# except ValueError:
#   print("Insira um valor válido")
# except ZeroDivisionError:
#   print("Número não pode ser dividido por zero")
# except:
#   print("Erro na operação...")
# finally:
#   print("Fim da operação!")

# Challenge Average
# Sabendo que a média do colégio é 7, crie um programa que receba as notas do aluno e verifique se foi aprovado ou reprovado. Imprima a média e a situação dele:

grade1 = float(input("Nota 1: "))
grade2 = float(input("Nota 2: "))

avg = (grade1 + grade2) / 2

if avg >= 7:
  print(f"Aluno aprovado com média {avg}")
else:
  print(f"Aluno reprovado com média {avg:.2f}")
