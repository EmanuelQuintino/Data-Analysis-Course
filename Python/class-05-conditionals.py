# Challenge Average
# Com base no array abaixo, imprima o nome do aluno e se ele foi aprovado ou reprovado com média maior ou igual a 7:
students_average_array = [
  { "name": "Pedro", "grade1": 5, "grade2": 8},
  { "name": "Ana", "grade1": 6.5, "grade2": 7},
  { "name": "Beatriz", "grade1": 8, "grade2": 10},
]

average1 = calc_avg(students_average_array[0]["grade1"], students_average_array[0]["grade2"])
average2 = calc_avg(students_average_array[1]["grade1"], students_average_array[1]["grade2"])
average3 = calc_avg(students_average_array[2]["grade1"], students_average_array[2]["grade2"])

print(f"{students_average_array[0]['name']} tem média igual a {average1}")
print(f"{students_average_array[1]['name']} tem média igual a {average2}")
print(f"{students_average_array[2]['name']} tem média igual a {average3}")
