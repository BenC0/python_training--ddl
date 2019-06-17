# ------------------------------------------------------------------------------
# Explanation
# Getting an input from the user can be an integral part of a scripts function
# Getting a user input is very straightforward in Python though. You just use
# the `input()` function
# ------------------------------------------------------------------------------

# Getting user input
# The below line will print "Please enter a value: " to the console and the
# script will pause while it waits for the user to type a value and press enter
# Note: Your question/input string will be displayed in verbatim, with no spaces
# between your string and the users input. To improve the UX of this, make sure
# to add some a space at the end of your string, and maybe a ":"
input("Please enter a value: ")

# Using a users input
# It's one thing to get a users input, but to actually use it we need to store
# the value in a variable. In true Pythonic fashion, this is fairly straightforward
# All you need to do is call the `input()` function and store it in a variable,
# like so.
userInput = input("Please enter a value: ")
# We can then use the users input however we'd like.
print("You typed {}!".format(userInput))