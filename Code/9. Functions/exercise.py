# ------------------------------------------------------------------------------
# Exercise
# 1. Fibonacci Sequence
# ------------------------------------------------------------------------------

# Exercise
# 1. Fibonacci Sequence
# The Fibonacci Sequence is a series of numbers made up from adding up the 2
# latest numbers in the sequence to find the next number.
# For example, the sequence starts with 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 and the
# next number in the sequence would be (21 + 34) 55.

# Write a function that gets a nth number in the Fibonacci Sequence
# for example:
# - calling fibonacci(1) should return "0"
# - calling fibonacci(2) should return "1"
# - calling fibonacci(4) should return "3"
# - calling fibonacci(6) should return "8"
# Hint: loops, basic operators and conditons will all be needed here.

def fibonacci(n):
	return n

print("calling 1 returns 0: " + fibonacci(1) == 0)
print("calling 2 returns 1: " + fibonacci(2) == 1)
print("calling 6 returns 8: " + fibonacci(6) == 8)
print("calling 12 returns 144: " + fibonacci(12) == 144)
print("calling 22 returns 17711: " + fibonacci(22) == 17711)