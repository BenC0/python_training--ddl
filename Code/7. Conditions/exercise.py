# ------------------------------------------------------------------------------
# Exercise
# 1. Amend the below variables so the IF statement prints True
# 2. Create the variables x, y and z and assign values to make the below IF
# statement print True
# ------------------------------------------------------------------------------

# Exercise
# 1. Amend the below IF statements so they print True

x = 0
y = [1, 2, 3]

if x == y:
	print("1.1", True)

a = "Hello World"
b = None
if a is b:
	print("1.2", True)

c = "A"
d = "Apple"
if c not in d:
	print("1.3", True)

if True is False:
	print("1.4", True)


# ------------------------------------------------------------------------------

# Exercise
# 2. Create the variables x, y and z and assign values to make the below IF
# statement print True

if (x is not y and z is x) and (y not in x):
	print("2.1", True)
