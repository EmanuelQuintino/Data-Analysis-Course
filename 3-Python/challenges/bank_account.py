class BankAccount:
  def __init__(self, balance = 0):
    self.balance = balance

  def check_balance(self):
    print(self.balance)

  def deposit(self, amount):
    self.balance += amount
    print(f"Novo depósito de {amount} com saldo de {self.balance}")

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"Novo saque de {amount} com saldo de {self.balance}")
    else:
      print("Saldo insuficiente!")

account = BankAccount(500)

print(account.balance)
account.check_balance()
account.deposit(100)
account.withdraw(200)
account.withdraw(100)
account.withdraw(400)
