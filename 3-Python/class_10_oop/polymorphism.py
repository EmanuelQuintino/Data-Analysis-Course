class Animal:
  def talk(self):
    pass

class Cat(Animal):
  def talk(self):
    return "Meow!"

class Dog(Animal):
  def talk(self):
    return "Woof!"

class Cow(Animal):
  def talk(self):
    return "Moo!"

cat = Cat()
dog = Dog()
cow = Cow()

print(cat.talk())
print(dog.talk())
print(cow.talk())
