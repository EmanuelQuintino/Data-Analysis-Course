num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação (+, -, /, *): ")

if operation == "+":
  result = num1 + num2
  print(f"A soma de {num1} e {num2} é {result}")

elif operation == "-":
  result = num1 - num2
  print(f"A subtração de {num1} e {num2} é {result}")

elif operation == "*":
  result = num1 * num2
  print(f"A multiplicação de {num1} e {num2} é {result}")

elif operation == "/":
  result = num1 / num2
  print(f"A divisão de {num1} e {num2} é {result:.2f}")

else:
  print("Operação inválida!")
