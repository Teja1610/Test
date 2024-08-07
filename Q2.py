# Create a dictionary with five key-value pairs
students_ages = {
    'Alice': 21,
    'Bob': 22,
    'Charlie': 20,
    'David': 23,
    'Eve': 19
}

# Access and print the age of a specific student
specific_student = 'Charlie'
age_of_student = students_ages[specific_student]
print(f"Age of {specific_student}: {age_of_student}")

# Add a new student to the dictionary
students_ages['Frank'] = 24

# Print the updated dictionary
print(f"Updated dictionary: {students_ages}")
