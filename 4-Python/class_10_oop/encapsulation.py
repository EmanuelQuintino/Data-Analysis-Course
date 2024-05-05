class User:
  def __init__(self, name, cpf):
    self.name = name
    self.__cpf = cpf
  
  def info(self):
    return self.name, self.__cpf
  

user = User("Emanuel Quintino", "123.123.123-12")

print(user.name)
# print(user.cpf) # error
print(user.info())
print(user.name)
user.info = "changed"
print(user.info)
