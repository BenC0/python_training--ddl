# ------------------------------------------------------------------------------
# Explanation
# Arithmetic Operators
# As with all other programming languages, you can basic operators to perform
# calculations
# String & List Operators
# You can also use the "+" and "*" operators to concatenate and multiply strings
# and lists
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Arithmetic Operators
# ------------------------------------------------------------------------------
# Mutiply values
calculation = 2 * 3
# prints (6)
print(calculation)

# Divide values
calculation = 4/2
# prints (2.0)
print(calculation)

# Addition and Subtraction
calculation = 1 + 2 - 1
# prints (2)
print(calculation)

# Modulo Operator %
# The modulo operator will return the integer remainder of a division
calculation = 11 % 3
# prints (2)
print(calculation)

# Power relationships
# You can use 2 multiplication symbols (**) to make a power relationship
squared = 7 ** 2
cubed = 2 ** 3
# prints (49 8)
print(squared, cubed)

# ------------------------------------------------------------------------------
# String Operators
# ------------------------------------------------------------------------------

# String Concatenation
hello = "Hello"
world = "World"
helloWorld =  hello + " " + world
# prints ("Hello World")
print(helloWorld)

# String multiplication
lotsofhellos = "hello" * 3
# prints (hellohellohello)
print(lotsofhellos)

# ------------------------------------------------------------------------------
# List Operators
# ------------------------------------------------------------------------------

# List Concatenation
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
# prints ([1, 3, 5, 7, 2, 4, 6, 8])
print(all_numbers)


# List multiplication
listA = [1, 2, 3]
listB = listA * 3
# prints ([1, 2, 3, 1, 2, 3, 1, 2, 3])
print(listB)