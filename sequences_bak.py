#!/usr/bin/env python

# The top line informs UNIX/LINUX that the current file should be executed 
# as a python script. Lines should never exceed 79 characters (see style
# guide).

"""Module Description
The docstring at the top of the file appears in the "Description" field of 
the help command. That is, if you load a python interpreter the following 
makes the docstring visible:
  $ python
  >>> import your_module
  >>> help(your_module)
Note the name "your_module" is just the filename without the .py extension.
You can check this field for any other python module (numpy, sympy, etc.) 
to get an idea about how module documentation is usually handled.
"""

# This is the body of the module.  Place all global constants, function 
# definitions, and class definitions here.  No free-floating executable
# code should appear in a module.

# Minimize the use of global constants.

def fibonacci(n):
	"""Function docstring
	All functions should have their own documentation via docstrings.
	Standard indent size in python is 4 spaces, no tabs. Arguments are
	positional, unless given a default value as a keyword-argument.
	Here args is a list of all positional arguments beyond those listed.
	Here kwargs is a list of all keyword arguments beyond those listed.
	"""
	
	#  check to make sure the input is valid
	try:         #https://wiki.python.org/moin/HandlingExceptions
		int(n)
	except ValueError as e:
		return 'Input is not a number' 

	if n < 1:
		raise 'Input is not a positive number'
	fibList=[1]
	fibCount = 1
	for index in range(1, n):
		fibList.append(fibCount)
		fibCount = fibCount + fibList[index-1]
	return fibList

def main(argv):
	"""Main function
	See below for why this would exist. The argv argument lists command
	line arguments taken from sys.argv in the main block below.
	"""
	test_fib1()
	test_fib2()
	test_fib3()
	test_fib4()
	test_fib5()
	pass

def test_fib1():
   # """Test function for nosetests
   # Any function starting with name test_ will be automatically run
   # by nosetests. Use an assert command to test a Boolean statement
   # about how your code executed.  If the assert fails, it throws
   # an exception, which is caught by nosetests and reported.
   # Anything that is printed to the screen during this function is
   # suppressed unless there is a failure, where it can be used for
   # debugging.
   # """
	expected = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875L
	fibList = fibonacci(1000)	
	computed = fibList[999]
	success = computed == expected
	msg = 'Computed %s, expected %s' % (computed, expected)
	assert success, msg 
	
def test_fib2():
   # """Test function for nosetests
   # Any function starting with name test_ will be automatically run
   # by nosetests. Use an assert command to test a Boolean statement
   # about how your code executed.  If the assert fails, it throws
   # an exception, which is caught by nosetests and reported.
   # Anything that is printed to the screen during this function is
   # suppressed unless there is a failure, where it can be used for
   # debugging.
   # """
	expected = [1]
	computed = fibonacci(1)
	success = computed == expected
	msg = 'Computed %s, expected %s' % (computed, expected)
	assert success, msg 

def test_fib3():
   # """Test function for nosetests
   # Any function starting with name test_ will be automatically run
   # by nosetests. Use an assert command to test a Boolean statement
   # about how your code executed.  If the assert fails, it throws
   # an exception, which is caught by nosetests and reported.
   # Anything that is printed to the screen during this function is
   # suppressed unless there is a failure, where it can be used for
   # debugging.
   # """
	expected = [1,1]
	computed = fibonacci(2)
	success = computed == expected
	msg = 'Computed %s, expected %s' % (computed, expected)
	assert success, msg 

def test_fib4():
   # """Test function for nosetests
   # Any function starting with name test_ will be automatically run
   # by nosetests. Use an assert command to test a Boolean statement
   # about how your code executed.  If the assert fails, it throws
   # an exception, which is caught by nosetests and reported.
   # Anything that is printed to the screen during this function is
   # suppressed unless there is a failure, where it can be used for
   # debugging.
   # """
	expected = 'Input is not a number' 
	computed = fibonacci('a')

	success = computed == expected
	msg = 'Computed %s, expected %s' % (computed, expected)
	assert success, msg 

def test_fib5():
   # """Test function for nosetests
   # Any function starting with name test_ will be automatically run
   # by nosetests. Use an assert command to test a Boolean statement
   # about how your code executed.  If the assert fails, it throws
   # an exception, which is caught by nosetests and reported.
   # Anything that is printed to the screen during this function is
   # suppressed unless there is a failure, where it can be used for
   # debugging.
   # """
	expected = 'Input is not a positive number'
	try:
		fibonacci(-1)
	except ValueError as e:
		computed = e

	success = computed == expected
	msg = 'Computed %s, expected %s' % (computed, expected)
	assert success, msg 
# After the body of the module, you can optionally create a section to
# house executable code.

if __name__ == "__main__":
	# This block only executes if the script is run as a standalone
	# program from the command line. It is not run when imported as
	# a module.
	
	# It is convention to call a single function here if possible
	# This function should be defined above and house all code to be
	# executed. Note that sys.argv will contain all commandline options.
	# The getopt module may also be helpful for more ambitious programs.
	from sys import argv
	main(argv)

