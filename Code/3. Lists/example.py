# ------------------------------------------------------------------------------
# Explanation
# In Python, an array is called a list. Other than that, lists are essentially
# the same as an array in JavaScript
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# List Declaration
# ------------------------------------------------------------------------------
# Declare an empty list
myEmptyList = []
# prints the empty list ("[]")
print(myEmptyList)

# Delcare a list with values
myList = ["Apples", "Oranges", "Grapes"]
# prints all values in the list ("['Apples', 'Oranges', 'Grapes']")
print(myList)

# ------------------------------------------------------------------------------
# Accessing a value within a list
# ------------------------------------------------------------------------------
myList = ["Apples", "Oranges", "Grapes"]
# prints the first value in the list ("Apples")
print(myList[0])
# prints the last value in the list ("Grapes")
print(myList[-1])

# ------------------------------------------------------------------------------
# Adding an item to a list
# ------------------------------------------------------------------------------
myList = []
myList.append("Apples")
# prints ("['Apples']")
print(myList)

# ------------------------------------------------------------------------------
# Get the index of a specific item in a list
# ------------------------------------------------------------------------------
myList = ["Apples", "Oranges", "Grapes"]
# prints ("1")
print(myList.index("Oranges"))

# ------------------------------------------------------------------------------
# Adding an item to a list at a specific index
# ------------------------------------------------------------------------------
myList = ["Oranges", "Grapes"]
myList.insert(0, "Apples")
# prints ("['Apples', 'Oranges', 'Grapes']")
print(myList)

# ------------------------------------------------------------------------------
# Removing an item from a list by specific value
# ------------------------------------------------------------------------------
myList = ["Apples", "Oranges", "Grapes"]
myList.remove("Apples")
# prints ("['Oranges', 'Grapes']")
print(myList)

# ------------------------------------------------------------------------------
# Removing an item from a list by specific index
# ------------------------------------------------------------------------------
myList = ["Apples", "Oranges", "Grapes"]
myPopValue = myList.pop(1)
# prints ("['Apples', 'Grapes']")
print(myList)
# prints ("Oranges")
print(myPopValue)

# ------------------------------------------------------------------------------
# Adding a list to a list
# ------------------------------------------------------------------------------
listA = ["Apples", "Oranges"]
listB = ["Grapes", "Kiwi"]
listA.extend(listB)
# prints ("['Apples', 'Oranges', 'Grapes', 'Kiwi']")
print(listA)