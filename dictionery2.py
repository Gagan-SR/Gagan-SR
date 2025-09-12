# Python Dictionary Example

# creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "CSE"
}

# displaying dictionary
print("Student Dictionary:", student)

# accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# adding a new key-value pair
student["college"] = "NMIT"
print("After adding college:", student)

# updating a value
student["age"] = 21
print("After updating age:", student)

# deleting a key
del student["course"]
print("After deleting course:", student)

# iterating through dictionary
print("All key-value pairs:")
for key, value in student.items():
    print(key, ":", value)
