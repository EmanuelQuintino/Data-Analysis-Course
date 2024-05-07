class Car:
  def __init__(self, brand, model, year, fipe):
    self.brand = brand
    self.model = model
    self.year = year
    self.fipe = fipe
  
  def info(self):
    return (self.brand, self.model, self.year, self.fipe)
  
  def sale(self, offer):
    if offer >= self.fipe:
      return "Carro vendido!"
    else:
      return "Não vendido!"

car1 = Car("Toyota", "SW4", "2024", 345000)
car2 = Car("Chevrolet", "Celta", "2006", 16500)

print(car1.brand)
print(car1.model)
print(car1.year)

print(car2.brand)
print(car2.info())
print(car2.sale(15000))
