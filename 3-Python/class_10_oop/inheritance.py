class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def info(self):
    return (f"User: {self.name} E-mail:{self.email}")

user = User("Emanuel Quintino", "emanuelquintino@gmail.com")
print(user.name)
print(user.email)
print(user.info())

class Admin(User):
  def __init__(self, name, email, status):
    super().__init__(name, email)
    self.status = status

admin = Admin("Emanuel Quintino", "emanuelquintino@gmail,com", "Master")
print(admin.name)
print(admin.email)
print(admin.info())
print(admin.status)
