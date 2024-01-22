class Calculator:
  def __add(self, num1, num2):
    return num1 + num2
  
  def __sub(self, num1, num2):
    return num1 - num2

  def calculate(self, num1, num2, operation):
    if operation == "+":
      result = self.__add(num1, num2)
      return f"A soma de {num1} e {num2} é {result}"

    elif operation == "-":
      result = self.__sub(num1, num2)
      return f"A subtração de {num1} e {num2} é {result}"
    
    else:
      print("Operação inválida!")

calculator = Calculator()
calculator.__add = "crashed"
print(calculator.__add)
print(calculator.calculate(2, 3, "+"))
print(calculator.calculate(2, 3, "-"))
