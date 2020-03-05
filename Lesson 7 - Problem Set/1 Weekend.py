# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if day.find('Saturday')!=-1:
       return True
    else:
       if day.find('Sunday')!=-1:
           return True
       else:
           return False

print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False
