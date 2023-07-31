class Vehicle:
  def __init__(self, model, year):
    self.model = model
    self.year = year

  def display_info(self):
    return (f"{self.model}({self.year})")

class Car(Vehicle):
  def __init__(self, model, year, test):
    super().__init__(model, year)
    self.test = test

class Motorcycle(Vehicle):
  pass

car = Car("Toyota-Corolla", 2022, "Test")
motorcycle = Motorcycle("Honda-CBR500R", 2023)

print(car.display_info())
print(car.test)
print(motorcycle.display_info())
