# Crie uma calculadora que calcule dois números e mostre o resultado
# O usuário deve fornecer além dos números a operação também (+, -, /, *)
# Ao final apresente uma mensagem com o resultado

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação (+, -, /, *): ")

if operation == "+":
  print(f"A soma de {num1} e {num2} é {num1 + num2}")

if operation == "-":
  print(f"A subtração de {num1} e {num2} é {num1 - num2}")

if operation == "*":
  print(f"A multiplicação de {num1} e {num2} é {num1 * num2}")

if operation == "/":
  print(f"A divisão de {num1} e {num2} é {(num1 / num2):.2f}")
  