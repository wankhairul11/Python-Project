# Function 1: Tuples
# Creating Tuples:
# Create a tuple called fruits containing the following elements: "apple", "banana", "cherry", "date".
# Print the first and last element of the tuple.

fruits = ("apple", "banana", "cherry", "date")
print(fruits[0], fruits[-1])
#output: apple, date

# Tuple Operations:
# Create a new tuple numbers with values (1, 2, 3, 4, 5).
# Use tuple unpacking to assign the first two elements of numbers to variables a and b, and the remaining elements to a variable rest.
# Print a, b, and rest.

numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers
print(a, b, rest)
#output: 1 2 [3, 4, 5]

# Tuple Immutability:
# Try to change the second element of the fruits tuple to "blueberry". Write down what happens and why.

try:
    fruits[1] = "blueberry"
except TypeError:
    print("Tuples are immutable, so you can't change their elements.")
#output: Tuples are immutable, so you can't change their elements.

# Function 2: Sets
# Creating Sets:
# Create a set called colors with the elements "red", "green", "blue", "yellow".
# Add the color "purple" to the set.

colors = {"red", "green", "blue", "yellow"}
colors.add("purple")
print(colors)
#output: {'red', 'green', 'blue', 'yellow', 'purple'}

# Set Operations:
# Create another set called primary_colors containing "red", "blue", and "yellow".
# Find the intersection of colors and primary_colors.
# Find the union of colors and primary_colors.
# Find the difference between colors and primary_colors.

primary_colors = {"red", "blue", "yellow"}
print("Intersection:", colors.intersection(primary_colors))
print("Union:", colors.union(primary_colors))
print("Difference:", colors.difference(primary_colors))
# output:
# Intersection: {'red', 'blue', 'yellow'}
# Union: {'red', 'yellow', 'blue', 'green', 'purple'}
# Difference: {'purple', 'green'}

# Set Membership:
# Check if "green" is in primary_colors. Print the result.
# Check if "orange" is not in colors. Print the result.

print("green" in primary_colors)        #output: False
print("orange" not in colors)           #output: True

# Function 3: Dictionary
# Creating Dictionaries:
# Create a dictionary called student_grades with the following key-value pairs:"Alice": 85
# "Bob": 90
# "Charlie": 78
# "Diana": 92
# Print the grade of "Bob".

student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}
print(student_grades["Bob"])
#output: 90

# Dictionary Operations:
# Add a new student "Eve" with a grade of 88 to the dictionary.
# Update "Alice"'s grade to 95.
# Remove "Charlie" from the dictionary.
# Print the updated dictionary.

student_grades["Eve"] = 88
student_grades["Alice"] = 95
del student_grades["Charlie"]
print(student_grades)
#output: {'Alice': 95, 'Bob': 90, 'Diana': 92, 'Eve': 88}

# Looping Through a Dictionary:
# Loop through the student_grades dictionary and print each student's name and grade in the format "Student: [name], Grade: [grade]".

for student, grade in student_grades.items():
    print(f"Student: {student}, Grade: {grade}")
# output:
# Student: Alice, Grade: 95
# Student: Bob, Grade: 90
# Student: Diana, Grade: 92
# Student: Eve, Grade: 88




