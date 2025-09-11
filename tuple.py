# Empty tuple
t1 = ()
print("Empty tuple:", t1)

# Tuple with integers
t2 = (1, 2, 3, 4, 5)
print("Tuple with numbers:", t2)

# Tuple with mixed data types
t3 = ("apple", 10, 3.5, True)
print("Mixed tuple:", t3)

# Nested tuple
t4 = (1, (2, 3), (4, 5))
print("Nested tuple:", t4)

# Creating tuple without parentheses (tuple packing)
t5 = 10, 20, 30
print("Tuple packing:", t5)

# Creating tuple from a list
my_list = [1, 2, 3]
t6 = tuple(my_list)
print("Tuple from list:", t6)

# Accessing elements
print("First element:", t2[0])
print("Last element:", t2[-1])
