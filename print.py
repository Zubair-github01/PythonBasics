# Basic print statement
print("Hello world")  

# Printing multiple values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Using f-strings
print(f"Name: {name}, Age: {age}")

# Using .format() method
print("Name: {}, Age: {}".format(name, age))

# Printing with separator
print("Python", "is", "awesome", sep=" - ")

# Printing with end parameter
print("Hello", end=" ")
print("World!")  # This will be printed on the same line

# Printing a list
fruits = ["Apple", "Banana", "Cherry"]
print("Fruits:", fruits)

# Printing special characters
print("This is a newline\nand this is a tab:\tHello!")

# Printing in a loop
for i in range(1, 6):
    print(f"Number {i}")

# Printing without newline
print("This is", end=" ")
print("on the same line.")

# Printing a dictionary
data = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", data)

# Using escape characters
print("She said, \"Python is great!\"")

# Printing a formatted table
print("\nTable Format:")
print("Name\tAge\tCity")
print("John\t30\tLondon")
print("Emma\t28\tParis")

