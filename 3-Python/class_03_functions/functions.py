def sum(num1, num2):
  total = num1 + num2
  print(total)

def sub(num1, num2):
  total = num1 - num2
  print(total)

def calc_avg(grade1, grade2):
  avg =  (grade1 + grade2) / 2
  return avg

sum(2, 3)
sum(4, 3)
sub(1, 5)
sub(3, 8)

student1_average = calc_avg(8.5, 7)
print(student1_average)

student2_average = calc_avg(6, 7)
print(student2_average)

# Challenge IMC
# Crie uma função que receba peso e altura dos pacientes e calcule seu IMC:
def calc_imc(height, weight):
  result = weight / height ** 2
  return result

print(f"{calc_imc(1.85, 82):.2f}")
