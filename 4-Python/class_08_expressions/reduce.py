# reduce

from functools import reduce

def sum(num1, num2):
  return num1 + num2

numbers = [200, 330, 350, 100]

print(reduce(sum, numbers))
print(reduce(lambda x, y: x + y, numbers))
