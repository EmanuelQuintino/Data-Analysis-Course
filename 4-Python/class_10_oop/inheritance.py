class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def info(self):
    return self.name, self.email

user = User("Emanuel Quintino", "emanuelquintino@gmail.com")

print(user.name)
print(user.email)
print(user.info())

class Admin(User):
  def __init__(self, name, email):
    super().__init__(name, email)
    self.status = "admin"

  def reports(self):
    return {
      "sale1": 1000,
      "sale2": 2000,
      "sale3": 3000,
    }

admin = Admin("Emanuel Quintino", "emanuelquintino@gmail,com")

print(admin.name)
print(admin.email)
print(admin.info())
print(admin.status)
print(admin.reports())
