#!/usr/bin/env python

from sys import argv
from sequences1 import fibonacci,main

def test_main():
	"""Test main function from sequences 1 exectued successfully"""
	arg = argv
	computed = main(arg)
	expected = None
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message	

def main(argv):
	pass


if __name__ == "__main__":	
	"""Call the fibonacci function from sequesces1 moduler"""
	try:
		n = argv[1]
		fibList=fibonacci(n)
	except IndexError:
		print 'No Command-line argument was inputed.'
		exit(1)
	if isinstance(fibList, list):
		print fibList[-1]
	else:
		print fibList
	
	
	main(argv)

	test_main()

