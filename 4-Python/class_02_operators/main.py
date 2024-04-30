# operators

num1 = 3
num2 = 2
num3 = -9.4

# arithmetic

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 % num2)
print(num1 // num2)
print(num3 ** (1/2))

print(pow(num1, num2))
print(abs(num3))
print(round(num3, 2))

print((num1 + num2) * num3)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
sum = num1 + num2

print(f"A soma de {num1} e {num2} é {sum}")

# assignment

num = 3
num = num + 2

num += 2
num -= 2
num *= 2
num /= 2
num %= 2
num **= 2
num //= 2

print(num)

# comparison

print(2 == 2)
print(2 == 3)
print(2 != 3)
print(2 != 2)
print(2 > 3)
print(2 < 3)
print(2 <= 3)
print(3 >= 3)
print(1 == "1")

# logical

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print(2 == 2 and 3 == 3)
print(2 != 2 and 3 == 3)
print(2 != 2 or 3 == 3)
print(2 != 2 or not 3 == 3)
