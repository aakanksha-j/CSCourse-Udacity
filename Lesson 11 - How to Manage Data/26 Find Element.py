# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p,q):
    i=0 
    while i<len(p): # for e in p
        if p[i]==q: #     if e==q:
            return i # everything same for both while loop and for loop except above two lines
        i=i+1
    return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
