# Capture dois números do usuário
# Faça as 4 operações (+, -, *, /) e atribua a variáveis semanticas
# Imprima na tela os dois números com operações e resultado

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print(type(num1))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print(f'''
  {num1} + {num2} = {add}
  {num1} - {num2} = {sub}
  {num1} * {num2} = {mul}
  {num1} / {num2} = {div:.2f}
''')
