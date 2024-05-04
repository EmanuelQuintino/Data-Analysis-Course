# map

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
