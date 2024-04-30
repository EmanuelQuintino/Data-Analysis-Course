# conditionals

age = 18
has_cnh = True

if age >= 18 and has_cnh:
  print("can drive")
else:
  print("can't drive")

if age >= 18 and age <= 70:
  print("vote required")
elif age < 16:
  print("can't vote")
else:
  print("optional vote")

# print(2/0)

try:
  print(2/"a")
except ValueError:
  print("invalid value!")
except ZeroDivisionError:
  print("cannot divided by zero!")
except:
  print("error!")
finally:
  print("end of operation!")

print("running...")