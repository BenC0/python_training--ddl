# ------------------------------------------------------------------------------
# Explanation
# Modules & Packages
# In programming, a module is a piece of software that has a specific
# functionality. For example, when building a ping pong game, one module would
# be responsible for the game logic, and another module would be responsible
# for drawing the game on the screen. Each module is a different file, which
# can be edited separately.
# ------------------------------------------------------------------------------

# import example_module using the below line (uncommented)
# import example_module
# import example_module using the below line and calling it calculator
import example_module as calculator_module

def calculator(a, b, method):
	method = method.lower()
	if method == "sum" or method == "+":
		# Call the sum function from the calculator module
		result = calculator_module.sum(a, b)
		formatted_method = "+"
	elif method == "minus" or method == "-":
		# Call the minus function from the calculator module
		result = calculator_module.minus(a, b)
		formatted_method = "-"
	elif method == "multiply" or method == "*":
		# Call the multiply function from the calculator module
		result = calculator_module.multiply(a, b)
		formatted_method = "*"
	elif method == "divide" or method == "/":
		# Call the divide function from the calculator module
		result = calculator_module.divide(a, b)
		formatted_method = "/"
	else:
		return "Method not recognized"
	return "The result of {a} {formatted_method} {b} is {result}".format(a=a, formatted_method=formatted_method, b=b, result=result)

def get_value_a():
	a = input("Please enter your first value: ")
	return calculator_module.handle_number_input(a)

def get_value_b():
	b = input("Please enter your second value: ")
	return calculator_module.handle_number_input(b)

def get_method():
	method = input("Please enter your method (sum|+, minus|-, multiply|* or divide|/): ")
	return method

def main():
	method = get_method()
	a = get_value_a()
	b = get_value_b()
	result = calculator(a, b, method)
	print(result)

# this means that if this script is executed, then main() will be executed
# automatically
if __name__ == '__main__':
    main()