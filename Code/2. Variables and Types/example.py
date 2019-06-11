# ------------------------------------------------------------------------------
# Explanation
# Python is completely object oriented, and not "statically typed". You do not
# need to declare variables before using them, or declare their type. Every
# variable in Python is an object.
# There are several types of variables, some of these are: integers, floating
# point numbers and strings
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Variable Declaration
# ------------------------------------------------------------------------------
# Declaring variables in Python is as simple as...
myVariable = "is a string"
print(myVariable)

# You can also declare multiple variables and their values on the same line
a, b = 3, 4
print(a, b)

# ------------------------------------------------------------------------------
# Types
# --------
# Please note: in the examples below we are checking the type of the variable 
# using the `type()` function and printing this alongside the variables value
# ------------------------------------------------------------------------------

# Integer
myInt = 1
print(myInt, type(myInt))

# To convert a string to an integer, call the `int()` function and pass the
# string to it
myStr = "1"
myConvertedInt = int(myStr)
print(myConvertedInt, type(myConvertedInt))

# ------------------------------------------------------------------------------

# Floating point numbers
myFloat = 1.0
print(myFloat, type(myFloat))

# To convert an integer to a float, call the `float()` function and pass the
# integer to it
myInt = 1
myConvertedFloat = float(myInt)
print(myConvertedFloat, type(myConvertedFloat))

# ------------------------------------------------------------------------------

# Strings
myStr = "bah"
print(myStr, type(myStr))

# To convert a value to a string, call the `str()` function and pass the value
# to it
myInt = 1
myConvertedStr = str(myInt)
print(myConvertedStr, type(myConvertedStr))

# To concatenate two strings, simply use the "+" opeartor
strA = "Hello"
strB = "World"
strC = strA + " " + strB
print(strC, type(strC))

# ------------------------------------------------------------------------------

# Boolean
myTrueBool = True
myFalseBool = False

print(myTrueBool, type(myTrueBool))
print(myFalseBool, type(myFalseBool))

# To convert a value to a Boolean, call the `bool()` function and pass the
# value to it
myStr = "Hello World"
myConvertedBool = bool(myStr)
print(myConvertedBool, type(myConvertedBool))

# ------------------------------------------------------------------------------

# None
# Sometimes, it's useful to declare an empty variable. To do this in Python,
# declare a variable as above, but asign it the value "None"
myEmptyVariable = None
print(myEmptyVariable, type(myEmptyVariable))
