class BankAccount:
  def __init__(self, balance = 0):
    self.__balance = balance

  def check_balance(self):
    print(self.__balance)

  def deposit(self, amount):
    self.__balance += amount
    print(f"Novo depósito de {amount} com saldo de {self.__balance}")

  def withdraw(self, amount):
    if amount <= self.__balance:
      self.__balance -= amount
      print(f"Novo saque de {amount} com saldo de {self.__balance}")
    else:
      print("Saldo insuficiente!")

account = BankAccount(500)

account.check_balance()
account.deposit(100)
account.withdraw(200)
account.withdraw(100)
account.withdraw(400)
