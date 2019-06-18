def sum(a, b):
	return a + b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a/b

def minus(a, b):
	return a - b

def handle_number_input(a):
	if "." in a:
		a = float(a)
	else:
		a = int(a)
	return a