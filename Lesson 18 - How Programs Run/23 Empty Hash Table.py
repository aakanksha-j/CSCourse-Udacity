# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    # return [[]]*3 wont work as all 3 empty buckets will refer to same empty object.
    table=[]
    for unused in range(0,nbuckets):
        table.append([])
    return table

print make_hashtable(5)==[[], [], [], [], []]
