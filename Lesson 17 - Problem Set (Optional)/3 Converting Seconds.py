# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(number):
    number_of_hours= int(number/3600)
    outputString= str(number_of_hours)
    if number_of_hours==1:
        outputString= outputString + " hour, "
    else:
        outputString= outputString + " hours, "
    number_of_minutes= int((number-(number_of_hours*3600))/60)
    outputString= outputString+ str(number_of_minutes)
    if number_of_minutes==1:
        outputString= outputString + " minute, "
    else:
        outputString= outputString + " minutes, "
    number_of_seconds= number-(number_of_hours*3600)-(number_of_minutes*60)
    outputString= outputString+ str(number_of_seconds)
    if number_of_seconds==1:
        outputString= outputString + " second, "
    else:
        outputString= outputString + " seconds, "
    return outputString    

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
