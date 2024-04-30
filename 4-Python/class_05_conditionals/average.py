# sabendo que a média do colégio é 7, crie um programa que receba as notas do aluno e verifique se foi aprovado ou reprovado

grade1 = float(input("nota 1: "))
grade2 = float(input("nota 2: "))

avg = (grade1 + grade2) / 2

if avg >= 7:
  print(f"aluno aprovado com média {avg}")
else:
  print(f"aluno reprovado com média {avg:.2f}")
