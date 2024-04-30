# conditionals

age = 18
# age = int(input("Digite sua idade: "))

has_cnh = True

if age >= 18 and has_cnh:
  print("pode dirigir")
else:
  print("não pode dirigir")

if age < 16:
  print("não pode votar")
elif age >= 16 and age < 18 or age > 70:
  print("voto facultativo")
elif age >= 18 and age <= 70:
  print("voto obrigatório")

try:
  num1 = float(input("Número 1: "))
  num2 = float(input("Número 2: "))
  print(num1/num2)
except ValueError:
  print("insira um valor válido!")
except ZeroDivisionError:
  print("número não pode ser dividido por zero")
except:
  print("erro na operação...")
finally:
  print("fim da operação!")
