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

# Operations on variables
# Variables can be used in mathematical operations.
# The result of the operation can be stored in a variable.

# Operations
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division
# // : Floor Division
# % : Modulus
# ** : Exponentiation

# Example
a = 10
b = 20
c = a + b
print(c)

# Output
# 30

# Example
a = 10
b = 20
c = a - b
print(c)

# Output
# -10

# Example
a = 10
b = 20
c = a * b
print(c)

# Output
# 200

# Example
a = 10
b = 20
c = a / b
print(c)

# Output
# 0.5

# Example
a = 10
b = 20
c = a // b
print(c)

# Output
# 0

# Example
a = 10
b = 20
c = a % b
print(c)

# Output
# 10

# Example
a = 10
b = 20
c = a ** b
print(c)

# Output
# 100000000

# Type conversion
# Variables can be converted from one data type to another data type.
# The data type of a variable can be converted using the following functions:
# int() : Converts a variable to an integer.
# float() : Converts a variable to a float.
# str() : Converts a variable to a string.
# bool() : Converts a variable to a boolean.

# Example
a = 10
b = float(a)
print(b)

# Output
# 10.0

# Example
a = 10.5
b = int(a)
print(b)

# Output
# 10

# Example
a = 10
b = str(a)
print(b)

# Output
# 10

# Example
a = "10"
b = int(a)
print(b)

# Output
# 10

# Example
a = "10.5"
b = float(a)
print(b)

# Output
# 10.5

# Example
a = "True"
b = bool(a)
print(b)

# Output
# True

# Example
a = "False"
b = bool(a)
print(b)

# Output
# False

# Example
a = 0
b = bool(a)
print(b)

# Output
# False

# Example
a = 1
b = bool(a)
print(b)

# Output
# True
