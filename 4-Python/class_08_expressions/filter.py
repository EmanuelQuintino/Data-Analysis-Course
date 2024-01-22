# Filter

def is_adult(student):
  if student["age"] >= 18:
    return True
  else:
    return False

students = [
  {"name": "João", "age": 30}, 
  {"name": "Carlos", "age":  15},
  {"name": "Joyce", "age": 17}, 
  {"name": "Francisco", "age":  23},
]

print(list(filter(is_adult, students)))
print(list(filter(lambda x: x["age"] >= 18, students)))
