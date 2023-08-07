class Person:
  def __init__(self, name, cpf):
    self.name = name
    self.__cpf = cpf
  
  def info(self):
    return self.name, self.__cpf

person = Person("Emanuel Quintino", "123.123.123-12")

print(person.name)
# print(person.cpf)
print(person.info())

class User(Person):
  pass

user = User("Emanuel Quintino", "789.789.789-78")

print(user.name)
user.info = "crashed"
print(user.info)
# print(user.info())
