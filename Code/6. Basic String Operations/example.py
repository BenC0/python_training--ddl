# ------------------------------------------------------------------------------
# Explanation
# Basic String Operations
# As with other languages, Python provides plenty of string operation functions
# ------------------------------------------------------------------------------

# Getting the length of a string
# To get the length of the a string, simply pass the string to the `len()`
# function
string = "Hello World!"
stringLength = len(string)
# prints (12)
print(stringLength)

# Getting the index of the first occurrence of a character in a string
# To get the index of a character in a string, use the `index()` function
# Note: This only gets the first occurrence of a string
string = "Hello World!"
# prints (4)
print(string.index("o"))

# Getting the number of times a character appears in a string
# To get the index of a character in a string, use the `count()` function
string = "Hello World!"
# prints (3)
print(string.count("l"))

# Slicing a string
# Slicing a string follows the same syntax as slicing a list.
string = "Hello World!"
# prints ("Hell")
print(string[0:4])
# You can take this a step further by including an additional argument in the
# square brackets. The below statement will print the characters from string
# but it will skip 2 characters. You can think of this syntax as `[start:stop:step]`
# prints ("Hl")
print(string[0:4:2])

# Reversing a string
# Reversing a string follows the same syntax as Slicing a string, except for the
# argument you pass to it. Using the additional slice argument from above, and
# changing the values to `[::-1]` will take the entire string and return it reversed
string = "Hello World!"
# prints ("!dlroW olleH")
print(string[::-1])
# This can also be used to get part of a string and reverse it.
# prints ("!dlroW")
print(string[12:5:-1])

# String formatting
# Converting a string to upper or lowercase is reasonably straightforward, you just
# call the `upper()` or `lower()` functions on the string
string = "Hello World!"
upperString = string.upper()
lowerString = string.lower()
# prints ("HELLO WORLD! hello world!")
print(upperString, lowerString)

# Checking the start and end of a string
# In true Python fashion, checking the start/end of a string for a substring is as
# simple as calling the `startswith()` and `endswith()` functions on the string,
# passing the substring to it. These functions return either true or false
string = "Hello World!"
startsWithHello = string.startswith("Hello")
endsWithBah = string.endswith("bah")
# prints (True False)
print(startsWithHello, endsWithBah)

# Splitting a string
# Splitting a string follows the same syntax as in JavaScript, just call the `split()`
# function and pass a string to it indicating where you want your split to happen
string = "Hello World!"
splitString = string.split(' ')
# prints (["Hello", "World!"])
print(splitString)