# Define a procedure,

# hashtable_update(htable,key,value)

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# Hint: Use hashtable_lookup as a starting point.
# Make sure that you return the new htable

def bucket_find(bucket,key):
    for entry in bucket:
        #print entry
        if entry[0]==key:
            #print entry
            return entry
    return None

def hashtable_update(htable,key,value):
    # Your code here
    entry = bucket_find(hashtable_get_bucket(htable, key), key)
    #print entry
    if entry:
        entry[1]=value
        print htable
        return htable
    hashtable_get_bucket(htable,key).append([key,value])
    return htable

def hashtable_lookup(htable,key):
    entry = bucket_find(hashtable_get_bucket(htable, key), key)
    if entry:
        return entry[1]
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [
         [['Francis', 13], ['Ellis', 11]],
         [['Andy', 5]], [['Bill', 17],['Zoe', 14]],
         [['Coach', 4]],
         [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]
        ]

print hashtable_lookup(table, 'Bill')
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42],
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2],
#>>> ['Rochelle', 94]]]
