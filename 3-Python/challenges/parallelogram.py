# Crie um programa que receba as medidas e calcule a área de um paralelogramo.
# O usuário deve fornecer os dados em metros através de um input.
# Ao final apresente uma mensagem com o resultado em m².

base = float(input("Digite a base: "))
height = float(input("Digite a altura: "))

area = base * height

print(f"O paralelogramo com base {base}m e com altura {height}m tem área de {area:.2f}m²")