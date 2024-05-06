class BankAccount:
  def __init__(self, balance = 0):
    self.__initial_balance = balance
    self.__balance = balance
    self.__transations = []

  def check_statement(self):
    print("=== Extrato Bancário ===")
    
    print("\nsaldo(=):", self.__initial_balance)
    
    for value in self.__transations:
      print(f"{value[0]}: {value[1]}")

    print("_________________")
    print("saldo(=):", self.__balance)

  def deposit(self, amount):
    self.__balance += amount
    self.__transations.append(["deposito(+)", amount])
    print(f"Novo depósito de {amount} com saldo de {self.__balance}")


  def withdraw(self, amount):
    if amount <= self.__balance:
      self.__balance -= amount
      self.__transations.append(["saque(-)", amount])
      print(f"Novo saque de {amount} com saldo de {self.__balance}")

    else:
      print("Saldo insuficiente!")

account = BankAccount(500)
waiting_for_input = False

while True:
  if waiting_for_input == True:
    input("\nPressione Enter para continuar...")
  
  print('\033[H\033[J')
  waiting_for_input = True

  print('''
===== Bank Account =====
  
  [1] Ver saldo
  [2] Fazer depósito
  [3] Fazer saque
  [4] Sair
      
========================  
  ''')

  option = input("\bEscolha uma opção: ")

  print("")

  if option == "1":
    account.check_statement()
  elif option == "2":
    amount = float(input("Digite o valor do depósito: "))
    account.deposit(amount)
  elif option == "3":
    amount = float(input("Digite o valor do saque: "))
    account.withdraw(amount)
  elif option == "4":
    print("Programa encerrado!\n")
    break
  else:
    print("Opção inválida!")
