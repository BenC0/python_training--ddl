# ------------------------------------------------------------------------------
# Explanation
# String Formatting
# Python uses C-style string formatting to create new, formatted strings. The
# "%" operator is used to format a set of variables enclosed in a "tuple" (a
# fixed size list), together with a format string, which contains normal text
# together with "argument specifiers", special symbols like "%s" and "%d".
# ------------------------------------------------------------------------------

# To use this in a string, simply include the %s operator within the string and
# after the string, write use the % operator again, followed by the variable
name = "John"
# prints ("Hello, John!")
print("Hello, %s!" % name)

# You can use this multiple times in the same string
name = "John"
age = 24
# prints ("John is 24 years old")
print("%s is %d years old" % (name, age)) # Note the brackets around the variables

# This can also be used with lists
myList = [1, 2, 3]
# prints ("myList is equal to [1, 2, 3]")
print("myList is equal to %s" % myList)

# Strings are included in the order in which they appear.
stringA = "hello"
stringB = "world"
# prints ("hello world")
print("%s %s" % (stringA, stringB))
# prints ("world hello")
print("%s %s" % (stringB, stringA))

# There are several different arguments you can use with the % operator.
# These are:
	# %s - String (or any object with a string representation, like numbers)

	# %d - Integers

	# %f - Floating point numbers

	# %.<number of digits>f - Floating point numbers with a fixed amount of
	# digits to the right of the dot.

string = "bah"
integer = 1
float1 = 0.1
float2 = 0.001
# prints ("my string is bah, my integer is 1, my first float is 0.100000 and my second float is 0.001")
print("my string is %s, my integer is %d, my first float is %f and my second float is %.3f" % (string, integer, float1, float2))