#!/bin/sh

#
# Script for St152 pracs S2/2004. Produces gnuplot output.
# Controlled by editing the sorts and max variables.
#
# Example Usage: 
#       ./runpy.sh > output.log ; gnuplot -persist output.log
#
# Authour: Andrew Turpin (andrew@cs.curtin.edu.au)
# Date:    August 2004
# Modified: Patrick Peursum
# Date:    September 2009
#


# The "sorts" variable contains a list of sort-array pairs that are passed
# to TestHarness
# First char: sort type
# - i = insertion sort
# - b  = bubble sort
# - s = selection sort
# - q = quicksort
# - m = mergesort
# - M = median of 3 pivot mergesort
# - R = random pivot mergesort
#
# Second char: initial order of array
# - a = ascending order
# - d = descending order
# - r = randomly ordered (actually: randomly swapped around)
# - n = ascending with 10% randomly swapped (ie: nearly sorted)
#
#sorts="ba bd br"
#sorts="ia id ir"
#sorts="sa sd sr"
#sorts="ma md mr"
#sorts="qa qd qr"
#sorts="Ma Md Mr"
#sorts="Ra Rd Rr"
#sorts="ba ia sa ma qa Ma Ra"
#sorts="bd id sd md qd Md Rd"
sorts="br ir sr mr qr Mr Rr"

# The "max" variable contains the maximum n that is passed to SortsTestHarness
max=8192
#max=1024


########################### DO NOT CHANGE BELOW THIS LINE ##################

tempFile="/tmp/st152$$"

runEm()
    {
    for i in `awk 'BEGIN{for(i=1;i<='"$max"';i*=2)print i;exit}'`
    do
        python SortsTestHarness.py $i $sorts
    done
    }


#runEm | sort +0 -1 +1n -2 > $tempFile
runEm > $tempFile

# PP: Following line is a fix for MacOSX sh not understanding the -n flag
# Unfortunately, it is incompatible with Linux
# Perhaps a proper solution is to do the full path /bin/echo ?
#echo "plot\c"
echo -n "plot"
echo $sorts | awk '{for(i=1;i<NF;i++)printf"\"-\" using 2:3 t \"%s\" w l,",$i}'
echo $sorts | awk '{i=NF;            printf"\"-\" using 2:3 t \"%s\" w l",$i}'
echo ""

for s in $sorts 
do
    grep "$s" $tempFile
    echo "e"
done
