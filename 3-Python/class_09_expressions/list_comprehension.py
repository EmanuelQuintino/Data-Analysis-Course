# List Comprehension

print([x for x in range(10)])

numbers = [2, 5, 6, 34, 11, 706, 85]
print([x for x in numbers if x % 2 == 0])


# Dict Comprehension

avgStudents = {"João": 60, "Carlos": 75, "Joyce": 80, "Francisco": 45}
print({k:v for k, v in avgStudents.items()})
print({k:("Aprovado" if v >= 70 else "Reprovado") for k, v in avgStudents.items()})
