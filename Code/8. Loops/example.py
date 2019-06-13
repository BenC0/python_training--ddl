# ------------------------------------------------------------------------------
# Explanation
# Loops
# There are two types of loops in Python, for and while.
# ------------------------------------------------------------------------------

# The "for" loop
# For loops iterate over a given sequence.
primeNumbers = [3, 5, 7]
for primeNumber in primeNumbers:
	# prints the items in the primeNumbers list separately, in the order they
	# appear
	print(primeNumber)

# We can also iterate over a sequence of numbers.
for x in range(5):
	# prints the numbers 0 - 4 in separate statements
	print(x)

# We can specify the range by passing an additional parameter to the function
for x in range(5, 10):
	# prints the numbers 5 - 9 in separate statements
	print(x)

# The "while" loop
# While loops repeat as long as a certain boolean condition is met
count = 0
while count < 5:
	# prints the numbers 0 - 4 in separate statements
	print(count)
	count += 1 # this is the same as count = count + 1

# The "break" and "continue" statements
# 'break' is used to exit a loop and 'continue' is used to skip the current block
# and return to the for/while statement
count = 0
while True:
	# prints the numbers 0 - 4 in separate statements
	print(count)
	count += 1
	if count >= 5:
		# ends the while loop
		break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
	# Check if x is even
	if x % 2 == 0:
		# ignores the rest of the code block
		continue
	print(x)

# The "else" clause
# We can also use the else clause in our for and if statement
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
	print(count)
	count +=1
else:
	print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
	if(i%5==0):
		break
	print(i)
else:
	print("this is not printed because for loop is terminated because of break but not due to fail in condition")