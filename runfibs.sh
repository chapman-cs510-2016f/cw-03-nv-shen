#!/bin/bash

# set the max loop size
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
#else
#	echo "File doesn't exist"
#	echo "No special handling"
fi

outString=''
newString=''
delim=','

#  run the script from 1 to maxFib
for ((index=1; index<=$maxFib;index=index+1))
do
	echo pass $index
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
echo $outString > $fibsFile

exit 0

