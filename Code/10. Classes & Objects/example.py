# ------------------------------------------------------------------------------
# Explanation
# Classes & Objects
# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes. Classes are essentially
# a template to create your objects.
# ------------------------------------------------------------------------------

# A very basic class would look something like this:
class MyClass:
	bah = "bah"
	# pass self to the function so you can access class variables within
	# the function
	def printMessage(self):
		print("This is a message inside the class.")

# You would then adign the class to an object by storing it in a variable.
# for example
myObject = MyClass()

# You can then access the bah variable like so
myObject.bah
# prints ("bah")
print(myObject.bah)

# You can also change the variable by reassigning it like so
myObject.bah = "foo"
# prints ("foo")
print(myObject.bah)

# You can call the function by calling...
# prints ("This is a message inside the class.")
myObject.printMessage()