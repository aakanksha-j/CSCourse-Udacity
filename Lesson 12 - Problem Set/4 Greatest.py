# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    if len(list_of_numbers)==0:
        return 0

    i=0
    temp=list_of_numbers[i]

    while i<len(list_of_numbers)-1:
        temp=bigger(temp,list_of_numbers[i+1])
        i=i+1
    return temp

def bigger(n1,n2):
    if n1>n2:
        return n1
    return n2

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
