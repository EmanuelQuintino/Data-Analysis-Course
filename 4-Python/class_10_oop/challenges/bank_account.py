class BankAccount:
  def __init__(self, balance = 0):
    self.__balance = balance
    self.__initial_balance = balance
    self.__file_path = "4-Python/class_10_oop/challenges/files/transactions.txt"
    self.__transactions = []
    self.__load_transactions()

  def __load_transactions(self):
    try:
      with open(self.__file_path, "r") as file:
        for line in file:
          transaction, amount = line.strip().split(", ")
          amount = float(amount)
          
          if transaction == "deposito(+)":
            self.__balance += amount
          elif transaction == "saque(-)":
            self.__balance -= amount
          
          self.__transactions.append((transaction, amount))
    
    except FileNotFoundError:
      print("arquivo não encontrado!")
      pass
    
  def check_statement(self):  
    print("=== Extrato Bancário ===")

    print("\nsaldo(=):", self.__initial_balance)
    
    for value in self.__transactions:
      print(f"{value[0]}: {value[1]}")

    print("_________________")
    print("saldo(=):", self.__balance)
  
  def __save_transactions(self, transaction, amount):
    try:
      with open(self.__file_path, "a") as file:
        file.write(f"{transaction}, {amount}\n")
    except FileNotFoundError:
      print("arquivo não encontrado!")
      pass

  def deposit(self, amount):
    self.__balance += amount
    self.__save_transactions("deposito(+)", amount)
    print(f"Novo depósito de {amount} com saldo de {self.__balance}")

  def withdraw(self, amount):
    if amount <= self.__balance:
      self.__balance -= amount
      self.__save_transactions("saque(-)", amount)
      print(f"Novo saque de {amount} com saldo de {self.__balance}")
    else:
      print("Saldo insuficiente!")

account = BankAccount()
waiting_for_input = False

while True:
  if waiting_for_input == True:
    input("\nPressione Enter para continuar...")
  
  # print('\033[H\033[J') # terminal clear
  waiting_for_input = True

  print('''
===== Bank Account =====
  
  [1] Ver extrato
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
