# abstraction
class User: 
  def __init__(self, name, cpf):
    self.name = name
    self.__cpf = cpf # encapsulation

  def get_cpf(self):
    return self.__cpf
  
  def info(self):
    return (self.name, self.__cpf)
  
user = User("Francisco", "000.000.000-00")
print(user.name)
# user.cpf = "xxxx"
# print(user.__cpf)
print(user.info())

# inheritance
class Admin(User):
  def __init__(self, name, cpf):
    super().__init__(name, cpf)
    self.__status = "admin"

  def set_status(self, status):
    self.__status = status 

  def get_status(self):
    return self.__status
  
  def info(self): # polymorphism
    return (self.name, self.get_cpf(), self.__status)
  
  def reports(self):
    if (self.__status == "gold"):
      return {
        "sale1": 1000,
        "sale2": 2000,
        "sale3": 3000,
      }
    else:
      return "sem autorização!"

admin = Admin("Natan", "111.111.111-11")
print(admin.name)
print(admin.get_status())
admin.set_status("gold")
print(admin.get_status())
print(admin.info())
print(admin.reports())
