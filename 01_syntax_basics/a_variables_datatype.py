"""
int is a data type that holds integer values. (e.g. 1, 2, 3, 4, 5)
float is a data type that holds floating point numbers. (e.g. 1.0, 2.0, 3.0, 4.0, 5.0)
str is a data type that holds strings. (e.g. "Hello", "World", "Python")
bool is a data type that holds boolean values. (e.g. True, False)
"""

# Variables
# Variables are used to store data values. A variable is created by assigning a value to it using the assignment operator (=).
# The value of a variable can be changed later in the program.
# Variables can be of different data types like int, float, str, bool, etc.

# Example
name = "Ridwan Halim"
age = 22
height = 160.5
is_male = True

# Printing variables
print(name)
print(age)
print(height)
print(is_male)

# Output
# Ridwan Halim
# 22
# 160.5
# True

# Assigning multiple values to multiple variables
name, age, height, is_male = "Ridwan Halim", 22, 160.5, True

# Printing variables
print(name)
print(age)
print(height)
print(is_male)

# Output
# Ridwan Halim
# 22
# 160.5
# True

# Assigning the same value to multiple variables
name = str(age)
print(name)

# Output
# 22

# Assigning the same value to multiple variables
name = str(age)
age = height
print(name)
print(age)

# Output
# 22
# 160.5

# Assigning the same value to multiple variables
name = age = height = 22
print(name)
print(age)
print(height)

# Output
# 22
# 22
# 22

# Assigning the same value to multiple variables
name = age
age = height
height = is_male
print(name)

# Output
# 22
# 160.5
# True
