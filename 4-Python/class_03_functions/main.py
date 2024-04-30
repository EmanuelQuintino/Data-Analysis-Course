def sum(num1, num2):
  total = num1 + num2
  return total

def sub(num1, num2):
  total = num1 - num2
  return total

print(sum(4, 3))
print(sum(2, 3))
print(sub(1, 5))
print(sub(3, 8))

def calc_avg(grade1 = 0, grade2 = 0):
  avg = (grade1 + grade2) / 2
  return avg

student1_average = calc_avg(8.5, 7)
print(student1_average)

student2_average = calc_avg(6, 7)
print(student2_average)
