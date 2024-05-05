class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def info(self):
    return self.model, self.year, self.brand
  
car = Car("Toyota", "Corolla", 2023)

print(car.brand)
print(car.model)
print(car.year)
print(car.info())
