#!/usr/bin/env python

#
### INSTRUCTOR COMMENT:
# sys is a module that should always be imported inside the __main__
# block at the bottom, since it is mostly appropriate for scripts.
#

from sys import argv

def main(argv):
	#
	### INSTRUCTOR COMMENT:
	# Note that you pass a string directly to fibonacci here. It would make much more
	# sense for fibonacci to take an integer input directly. The conversion to a string
	# is a task for a separate function that "sanitizes" the input. You want each function
	# to do one thing well. In this case, fibonacci should only compute the fibonacci
	# sequence. It should not also handle messy details about type formatting.
	#
	print fibonacci(argv[1])
	#
	### INSTRUCTOR COMMENT:
	# This convention of returning an int is good, but you have to use the value later if
	# you do so. The reason for this is so you don't have to call sys.exit() outside of a
	# __main__ block. Instead, you return the exit code, and then exit with that exit code
	# only inside the __main__ block below.
	#
	return 0

def fibonacci(number):
	"""Enter a positive interger, return a fibonacci list"""
	#
	### INSTRUCTOR COMMENT:
	# As noted above, this sort of input sanitation should not be in
	# such a simple function. Separate concerns. Simplify. (Also, it's
	# spelled "integer" in your docstring.)
	# The only test that makes sense to do here is a type check that the
	# input is a positive integer. Something like: 
	#     if not (isinstance(number, int) and number > 0): 
	#         raise TypeError("Not a positive integer")
	#
	try:
		number = int(number)
	except IndexError:
		return 'Argument must be supplied on the command line.'
	except TypeError:
		return 'Argument must not be a list'
	except ValueError:
		return 'Argument must be a integer, not "%s"' % number
	
	if number < 1:
		return 'Argument must be a positive integer, not %d' % number
	else:
		#
		### INSTRUCTOR COMMENT:
		# It is suboptimal to put the main block of code in a function
		# so indented. That is usually a sign that you should simplify your
		# logic. Using the assert check above, all of below can become 
		# the entire function block.
		#
		fibList = [1]
		fibNum = 1
		for index in range(1,number):
			fibList.append(fibNum)
			fibNum += fibList[index-1]
		return fibList

def test_fibonacci_normal():
	"""Fibonacci number is between 1 to 1000. """
	#
	### INSTRUCTOR COMMENT:
	# Note: if you see yourself copying and pasting large blocks
	# of code like in the following three test functions, there is 
	# usually a better coding approach. For example, you could abstract
	# away this structure into a helper function:
	#     def comparison(computed, expected):
	#         message = 'Computed {}, expected {}'.format(computed, expected)
	#         assert computed == expected, message
	#
	# Then this function and others would simplify to (no duplicated code):
	#     def test_fibonacci_normal():
	#         comparison(fibonacci(5), [1,1,2,3,5])
	#
	number = 5
	computed = fibonacci(number)
	expected = [1,1,2,3,5]
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected) 
	assert success, message

def test_fibonacci_negNum():
	"""Fibonacci number is a negative number """
	number = -10
	computed = fibonacci(number)	
	expected = 'Argument must be a positive integer, not -10'
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

def test_fibonacci_char():
	"""Fibonacci number is a char"""
	number = 'a'
	computed = fibonacci(number)
	expected = 'Argument must be a integer, not "a"'
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message


	

if __name__ == "__main__":
	try:
		main(argv)
	except IndexError:
		print 'No Command-line argument was inputed.'
		exit(1)
	# test function
	#
	### INSTRUCTOR COMMENT:
	# Use nose to run your tests, rather than hard-coding them into
	# __main__ blocks like this. The reason is that nose inspects your code
	# and runs all tests it finds, even if you forget to update your __main__
	# block later.
	#
	test_fibonacci_normal()
	test_fibonacci_negNum()
	test_fibonacci_char()
