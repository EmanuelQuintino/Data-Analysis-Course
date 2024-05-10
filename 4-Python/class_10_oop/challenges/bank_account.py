class Bank_account:
  def __init__(self, balance = 0):
    self.__balance = balance
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
    
    except:
      print("arquivo não encontrado!")
      pass

  def __save_transactions(self, transaction, amount):
    try:
      with open(self.__file_path, "a") as file:
        file.write(f"{transaction}, {amount}\n")
    except:
      print("arquivo não encontrado!")
      pass

  def check_statement(self):  
    print("=== Extrato Bancário ===\n")
    
    for value in self.__transactions:
      print(f"{value[0]:>11}: {value[1]:>11.2f}")

    print("\n========================")
    print(f"{'saldo(=)':>11}: {self.__balance:>11.2f}")
    print("========================")
  
  def deposit(self, amount):
    self.__balance += amount
    self.__save_transactions("deposito(+)", amount)
    self.__transactions.append(("deposito(+)", amount))
    print(f"Novo depósito de R${amount:.2f}!")

  def withdraw(self, amount):
    if amount == 0:
      return print("Saque deve ser maior que zero!")
    
    if amount <= self.__balance:
      self.__balance -= amount
      self.__save_transactions("saque(-)", amount)
      self.__transactions.append(("saque(-)", amount))
      print(f"Novo saque de R${amount:.2f}!")
    else:
      print("Saldo insuficiente!")

account = Bank_account()
waiting_menu = False # flag

while True:
  if waiting_menu == True:
    input("\nPressione Enter para continuar...")

  # print('\033[H\033[J') # terminal clear
  print("\033c", end="") # terminal clear
  waiting_menu = True

  print('''
=== Automated Teller Machine ===
  
  [1] Ver extrato
  [2] Fazer depósito
  [3] Fazer saque
  [4] Sair
      
================================  
  ''')

  option = input("\bEscolha uma opção: ")

  print("")

  if option == "1":
    account.check_statement()
  elif option == "2":
    amount = float(input("Digite o valor do depósito: R$"))
    account.deposit(amount)
  elif option == "3":
    amount = float(input("Digite o valor do saque: R$"))
    account.withdraw(amount)
  elif option == "4":
    print("Programa encerrado!\n")
    break
  else:
    print("Opção inválida!")
