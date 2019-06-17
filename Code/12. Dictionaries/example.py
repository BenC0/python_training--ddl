# ------------------------------------------------------------------------------
# Explanation
# A dictionary is a data type similar to arrays, but works with keys and values
# instead of indexes. Each value stored in a dictionary can be accessed using a
# key, which is any type of object (a string, a number, a list, etc.) instead
# of using its index to address it.
# ------------------------------------------------------------------------------

# Declaring a dictionary
# To declare an empty dictionary, asign a variable the value of "{}"
myDictionary = {}

# To declare a dictionary with values, you follow a similar syntax
myDictionary = {
	"prop1": "value1",
	"prop2": "value2",
	"prop3": "value3"
}
# prints ("{'prop1': 'value1', 'prop2': 'value2', 'prop3': 'value3'}")
print(myDictionary)

# A more usable example would be a phonebook
phonebook = {
	"Jack": "01617986355",
	"John": "01617980480",
	"Jill": "07455232079"
}

# Iterating over dictionaries
# You can easily iterate over dictionaries using a for...in... loop. e.g.
# Note: With the for...in... loop, you define 2 variables. 1 for the property
# and a second for the value.
for name, number in phonebook.items(): # using the `.items()` function
	print("%s's phone number is %s" % (name, number))

# Adding a value
# Adding a value is fairly straightforward. 
phonebook["Jake"] = "0124567890"
# prints ("{'Jack': '01617986355', 'John': '01617980480', 'Jill': '07455232079',
# 'Jake': '0124567890'}")
print(phonebook)

# Removing a value
# To remove a value from the dictionary, we have 2 methods. One is to use `del`
# the second is to use `.pop()`, both are shown below

# del
phonebook = {
	"Jack": "01617986355",
	"John": "01617980480",
	"Jill": "07455232079"
}

del phonebook["Jack"]
# prints ("{'John': '01617980480', 'Jill': '07455232079'}")
print(phonebook)

# .pop()
phonebook = {
	"Jack": "01617986355",
	"John": "01617980480",
	"Jill": "07455232079"
}

phonebook.pop("Jack")
# prints ("{'John': '01617980480', 'Jill': '07455232079'}")
print(phonebook)