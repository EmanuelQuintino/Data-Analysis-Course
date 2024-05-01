# Crie um programa que receba duas notas do aluno
# Faça uma função que calcule a sua média
# Apresente na tela SE o aluno foi aprovado (média 7)
# Trate os possíveis error na aplicação

def calc_avg(grade1, grade2):
  if grade1 < 0 or grade1 > 10 or grade2 < 0 or grade2 > 10:
    raise ValueError("Nota fora do intervalo de 0 a 10!")
  
  return (grade1 + grade2) / 2 

try:
  student_grade1 = float(input("Nota 1: "))
  student_grade2 = float(input("Nota 2: "))

  avg = round(calc_avg(student_grade1, student_grade2), 2)

  if avg >= 7:
    print(f"Aprovado com {avg}")
  else:
    print(f"Reprovado com {avg}")
    
except ValueError as Error:
  print(f"Valor inválido!")
  print(Error)
except:
  print("Erro operação!")
