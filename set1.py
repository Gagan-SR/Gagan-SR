# creating a set
my_set = {1, 2, 3, 4, 4, 5}

print("Original set:", my_set)   # Duplicates are removed

# adding elements
my_set.add(6)
print("After adding 6:", my_set)

# removing elements
my_set.remove(2)
print("After removing 2:", my_set)

# set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a | set_b)          # or set_a.union(set_b)
print("Intersection:", set_a & set_b)   # or set_a.intersection(set_b)
print("Difference:", set_a - set_b)     # or set_a.difference(set_b)
