# Exercise 1: Below are the two lists convert it into the dictionary
# Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# solution 1
dct = dict()
for index in range(len(keys)):
    dct[keys[index]] = values[index]
# solution 2
dct = dict(zip(keys, values))


# Exercise 2: Merge following two Python dictionaries into one
# Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Solution 1
dict1.update(dict2)

# Solution 2
keys = set(dict1.keys())
keys.update(dict2.keys())
dct = dict()
for k in keys:
    dct[k] = dict1.get(k, None) or dict2.get(k, None)
print(dct)


# Exercise 3: Access the value of key ‘history’ from the below
# Output: 80
dict_ex3 = {
   "class": {
      "student": {
         "name": "Mike",
         "marks": {
            "physics": 70,
            "history": 80
         }
      }
   }
}

print(dict_ex3["class"]["student"]["marks"]["history"])
print(dict_ex3.get("class", {}).get("student", {}).get("marks", {}).get("history", None))


# Exercise 4: Create a new dictionary by extracting the following keys from a below dictionary
# Output: {'name': 'Kelly', 'salary': 8000}
keys_to_extract = ["name", "salary"]
dict_ex4 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Solution 1
res_ex4 = dict()
for key in keys_to_extract:
    res_ex4[key] = dict_ex4[key]
print(res_ex4)

# Solution 2
print({k: v for k, v in dict_ex4.items() if k in keys_to_extract})


# Exercise 5: Delete set of keys from a dictionary
# Output: {'city': 'New york', 'age': 25}
keys_to_remove = ["name", "salary"]
dict_ex5 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Solution 1
for key in keys_to_remove:
    del dict_ex5[key]
print(dict_ex5)

# Solution 2
print({k: v for k, v in dict_ex4.items() if k not in keys_to_remove})


# Exercise 6: Check if a value 200 exists in a dictionary
# Output: True
dict_ex6 = {'a': 100, 'b': 200, 'c': 300}

# Solution 1
print(200 in dict_ex6.values())

# Solution 2
exists = False
for value in dict_ex6.values():
    if value == 200:
        exists = True
        break
print(exists)


# Exercise 7: Rename key city to location in the following dictionary
# Output: {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "location": "New york"
# }
dict_ex7 = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}

# Solution 1
dict_ex7["location"] = dict_ex7.pop("city")

# Solution 2
temp = dict_ex7["city"]  # "New york"
del dict_ex7["city"]
dict_ex7["location"] = temp


# Exercise 8: Get the key of a minimum value from the following dictionary
# Output: Math
dict_ex8 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# Solution 1
min_value_key = dict_ex8.keys()[0]
min_value = dict_ex8[min_value_key]
for k, v in dict_ex8.items():
    if v < min_value:
        min_value_key = k
        min_value = v
print(min_value_key)
print(min_value)


# Exercise 9: Change Brad’s salary to 8500 from a given Python dictionary
# Output: {
#      'emp1': {'name': 'John', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 8500}
# }
dict_ex9 = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

# Solution 1
dict_ex9["emp3"]["salary"] = 8500

# Solution 2
for key, employee in dict_ex9.items():  # (key, val)
    if employee['name'] == 'Brad':
        employee['salary'] = 8500
        break
print(dict_ex9)
