# ------------------------------------------------------------------------------
# Explanation
# Conditions
# Python uses boolean variables to evaluate conditions. The boolean values True
# and False are returned when an expression is compared or evaluated
# ------------------------------------------------------------------------------

# When comparing values we use either the double equals operator, "==", or the
# "not equals" operator, "!=". We are also able to make use of the other 
# comparison operators. These are:
# "==" - Equals
# "!=" - Not Equals
# "<>" - Not Equals
# ">" - Greater Than
# "<" - Less Than
# ">=" - Greater Than or Equal to
# "<=" - Less Than or Equal to
# Note: Unlike JavaScript, there is no triple equals operator "==="

x = 2
# prints out True
print(x == 2)
# prints out False
print(x == 3)
# prints out True
print(x < 3)
# prints out False
print(x > 3)

# If Statements
# If statements in python generally follow the same syntax as other languages
# with some minor differences. Please see the example below.
if 1 == 2:
	print("1 is equal to 2?")
elif 1 != 2:
	print("1 is not equal to 2!")
else:
	print("I have no idea how numbers work :'(")

# You'll notice in the above example that we don't use any brackets in our IF
# statement. This is because Python relies on indentation to separate blocks
# of code.

# Boolean operators
# In Python, you can use the "and" and "or" boolean operators to build complex
# expressions. See the IF statement example below.

name = "John"
age = 23

if name == "John" and age == 23:
	print("You're name is John and you're 23 years old")

if age == 23 or age == 24:
	print("You're 23 or 24 years old")

# The "in" operator
# You can also use the "in" operator to check if a value is in a list
name = "John"

if name in ["John", "Bob"]:
	print("You're name is either John or Bob")

# You can also do this with strings.
name = "John"
if "J" in name:
	print("J is in %s!" % name)

# The "is" operator
# Unlike the double equals operator "==", the "is" operator does not match
# the values of the variables, but the instances themselves.
x = [1,2,3]
y = [1,2,3]
z = x
# Prints out True
print(x == y)
# Prints out False
print(x is y)
# Prints out True
print(z is x)

# The "not" operator
# You can use the "not" operator before a boolean expression to invert it
# prints (True)
print(not False)
myList = [1,2,3]
# prints ("4 is not in myList")
if 4 not in myList:
	print("4 is not in myList")