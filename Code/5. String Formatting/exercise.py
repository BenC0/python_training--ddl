# ------------------------------------------------------------------------------
# Exercise
# ------------------------------------------------------------------------------

# Exercise
# 1. Alter the code below so the print statement prints the below statement
	# "Hello John, you're current balance is £0.40. That's depressing."

data = ["John", "Hello", 0.4]
formatString = "%s, you're current balance is £. That's depressing."
print(formatString % (data[0]))