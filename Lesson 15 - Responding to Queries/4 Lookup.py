# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index1 = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index1,keyword):

    j=0
    while j<len(index1):
        if keyword==index1[j][0]:
            return index1[j][1]
        j=j+1
    return []

print lookup(index1,'udacity')
#>>> ['http://udacity.com','http://npr.org']
