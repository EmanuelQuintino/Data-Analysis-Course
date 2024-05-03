# Crie uma função que receba um número como parâmetro e calcule seu fatorial

def factor(num):
  total = 1
  # while num > 0:
  #   total *= num
  #   num -= 1

  for value in range(num, 1, -1):
    total *= value
  
  return total


def factor_r(num):
  if num == 1:
    return 1
  
  return num * factor_r(num - 1)

print(factor(5))
print(factor_r(5))
