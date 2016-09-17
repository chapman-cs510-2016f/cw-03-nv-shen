#!/usr/bin/env python

from sys import argv

def main(argv):
	print fibonacci(argv[1])
	return 0

def fibonacci(number):
	"""Enter a positive interger, return a fibonacci list"""
	try:
		number = int(number)
	except IndexError:
		return 'Argument must be supplied on the command line.'
	except TypeError:
		return 'Argument must not be a list'
	except ValueError:
		return 'Argument must be a number, not "%s"' % number
	
	if number < 1:
		return 'Argument must be a positive integer, not %d' % number
	else:
		fibList = [1]
		fibNum = 1
		for index in range(1,number):
			fibList.append(fibNum)
			fibNum += fibList[index-1]
		return fibList

def test_fibonacci_normal():
	"""Fibonacci number is between 1 to 1000. """
	number = 5
	computed = fibonacci(number)
	expected = [1,1,2,3,5]
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected) 
	assert success, message

def test_fibonacci_negNum():
	"""Fibonacci number is a negative number """
	number = -10
	try:
		fibonacci(number)	
	except ValueError as e:
		print e
		computed = e
	expected = 'Argument must be a positive integer, not -10'
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

def test_fibonacci_char():
	"""Fibonacci number is a char"""
	number = 'a'
	try:
		fibonacci(number)	
	except ValueError as e:
		computed = e
	expected = 'Argument must be a number, not "a"'
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
	#test_fibonacci_normal()
	#test_fibonacci_negNum()
	#test_fibonacci_char()