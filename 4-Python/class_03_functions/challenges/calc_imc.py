# Defina uma função que retorne o IMC do usuário
# Receba via input altura e peso e passe via argumentos

def calc_imc(height, weight):
  imc = weight / (height * height)
  return imc

height = float(input("Digite sua altura(m): "))
weight = float(input("Digite seu peso(kg): "))
imc = calc_imc(height, weight) 

print(f"Seu IMC é {imc:.2f}")