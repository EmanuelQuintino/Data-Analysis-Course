class Student():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def matriculate(self):
    print(f"{self.name} matriculado(a) com sucesso!")

student = Student("Emanuel", "30")
print(student.name)
print(student.age)
student.matriculate()
