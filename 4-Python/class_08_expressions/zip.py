# zip

array1 = [1, 2, 3]
array2 = [4, 5, 6]

dict1 = {1: "A", 2: "B"}
dict2 = {3: "C", 4: "B"}

print(list(zip(array1, array2)))
print(list(zip(dict1.values(), dict2)))
