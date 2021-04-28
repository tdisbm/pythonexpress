# Exercise 1: Add a list of elements to a given set
# Output: {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
set_ex1 = {"Yellow", "Orange", "Black"}
list_ex1 = ["Blue", "Green", "Red"]

# Solution 1
set_ex1.update(list_ex1)

# Solution 2
for to_add in list_ex1:
    set_ex1.add(to_add)


# Exercise 2: Return a new set of identical items from a given two set
# Output: {40, 50, 30}
set1_ex2 = {10, 20, 30, 40, 50}
set2_ex2 = {30, 40, 50, 60, 70}

res_ex2 = set_ex1.intersection(set1_ex2)


# Exercise 3: Returns a new set with all items from both sets by removing duplicates
# Output: {70, 40, 10, 50, 20, 60, 30}
set1_ex3 = {10, 20, 30, 40, 50}
set2_ex3 = {30, 40, 50, 60, 70}

set1_ex3.union(set2_ex3)


# Exercise 4: Given two Python sets, update the first set with items that exist only in the first set and not
# in the second set.
# Output: {10, 30}
set1_ex4 = {10, 20, 30}
set2_ex4 = {20, 40, 50}

set1_ex4.difference_update(set2_ex4)


# Exercise 5: Remove items 10, 20, 30 from the following set at once
# Output: {40, 50}
set1_ex5 = {10, 20, 30, 40, 50}

set1_ex5.difference_update({10, 20, 30})


# Exercise 6: Return a set of all elements in either A or B, but not both
# Output: {20, 70, 10, 60}
set1_ex6 = {10, 20, 30, 40, 50}
set2_ex6 = {30, 40, 50, 60, 70}

set1_ex6.symmetric_difference(set2_ex6)


# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements.
# Output: {10}
set1_ex7 = {10, 20, 30, 40, 50}
set2_ex7 = {60, 70, 80, 90, 10}

print(set1_ex7.intersection(set2_ex7))


# Exercise 8: Update set1 by adding items from set2, except common items
# Output: {70, 10, 20, 60}
set1_ex8 = {10, 20, 30, 40, 50}
set2_ex8 = {30, 40, 50, 60, 70}

set1_ex8.symmetric_difference_update(set2_ex8)


# Exercise 9: Remove items from set1 that are not common to both set1 and set2
# Output: {40, 50, 30}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection(set2)
