#!/bin/bash

# set the max loop size
#
### INSTRUCTOR COMMENT:
# The bash convention for global variables is to make them all caps: MAXFIB etc.
#
maxFib=10000
fibsFile=./fibs.csv
fibsFileBak=./fibs.csv.bak


# file and file backup checking
# check if the target file exists
if [ -f $fibsFile ]; then
	# if the file exists, check for the back up file existing
	if [ -f $fibsFileBak ]; then
		echo "Both $fibsFile and $fibsFileBak exist"
		echo "Terminating run"
		exit 1 
	else
		# make a backup of the file
		echo "Moved $fibsFile to $fibsFileBak to backup the file"
		echo "Continuing with run"
		mv $fibsFile $fibsFileBak
	fi
fi

outString=''
newString=''
delim=','

#  run the script from 1 to maxFib
#
### INSTRUCTOR COMMENT:
# While this numerical style of for loop is possible, it is rare in bash.
# Usually just iterating over the elements of something like $(seq) is more clear
#
for ((index=1; index<=$maxFib;index=index+1))
do
# command output captured into a variable is from (this was difficult to track down, and many harder ways to do it)
# http://stackoverflow.com/questions/4651437/how-to-set-a-variable-equal-to-the-output-from-a-command-in-bash
#  Note that the quotations are required to capture multi-line values.  No quotes captures just the last line apparently.
#  Left the quotes in as a better example.
	newString="$(python ./fib.py $index)"
	if [ $index -eq 1 ]
	then
		#  no leading delimiter, this is the first entry
		outString=$newString
	else
		#  all subsequent entries need a delimiter
		outString=$outString$delim$newString
	fi
done
#  note that there is no trailing delimiter after the final numeric entry

#  put our comma-delimited fib string into the output data file
#
### INSTRUCTOR COMMENT:
# Note that it's also possible to append (>>) to a file at each iteration,
# rather that collecting a giant string in memory and then dumping it all at once.
#
echo $outString > $fibsFile

#
### INSTRUCTOR COMMENT:
# No need to exit 0. It's automatic.
exit 0

