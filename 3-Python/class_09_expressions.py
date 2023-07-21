# Lambda

sqr2 = lambda num: num ** 2
oprSum = lambda num1, num2: num1 + num2

print(sqr2(3))
print(oprSum(3, 2))

# List Comprehension

print([x for x in range(10)])

numbers = [2, 5, 6, 34, 11, 706, 85]
print([x for x in numbers if x % 2 == 0])


# Dict Comprehension

avgStudents = {"João": 60, "Carlos": 75, "Joyce": 80, "Francisco": 45}
print({k:v for k, v in avgStudents.items()})
print({k:("Aprovado" if v >= 70 else "Reprovado") for k, v in avgStudents.items()})

# Map

def pow(num):
  return num ** 2

def fahrenheit(celsius):
  return 9 / 5 * celsius + 32

numbers = [1, 3, 4, 67, 8, 10]

print(list(map(pow, numbers)))
print(list(map(lambda num: num ** 2, numbers)))

print(list(map(fahrenheit, numbers)))
print(list(map(lambda celsius: 9 / 5 * celsius + 32, numbers)))

numbers1 = [2, 4, 5, 8]
numbers2 = [4, 3, 12, 6]

print(list(map(lambda x, y: x + y, numbers1, numbers2)))
