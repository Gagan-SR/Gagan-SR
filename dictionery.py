# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "CSE",
    "marks": 85
}

# Display dictionary
print("Student Dictionary:", student)

# Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["college"] = "NMIT"
print("After adding college:", student)

# Updating an existing value
student["marks"] = 90
print("After updating marks:", student)

# Removing a key-value pair
removed = student.pop("age")
print("Removed Age:", removed)
print("After removal:", student)

# Iterating through dictionary
print("\nIterating through dictionary:")
for key, value in student.items():
    print(key, ":", value)
