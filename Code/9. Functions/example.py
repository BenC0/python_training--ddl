# ------------------------------------------------------------------------------
# Explanation
# Functions
# ------------------------------------------------------------------------------

# functions in Python are defined using the below syntax
def myFunction():
	print('Hello, this is myFunction!')

# functions are then called using the below syntax
myFunction() # prints 'Hello, this is myFunction!'

# function can take parameters, to do this you need to define your function with
# parameters.
def sum(a, b):
	return a + b

# You would then use this function like so
sum(1, 2) # returns 2

# To make this more useful, we can store use variables
a = 1
b = 2
x = sum(a, b)
print("x is equal to %d" % x) # prints "x is equal to 3"

# generally functions work the same in Python as they do in JavaScript.
# Further examples below.

def squareNumber(x):
	return x ** 2

def sum(a, b):
	return a + b

a = squareNumber(2) # returns 4
b = squareNumber(4) # returns 16
c = sum(a, b) # returns 20
print("c is equal to %d" % c) # prints "c is equal to 20"