# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

from Bad_Hash import test_hash_function

def hash_string(keyword,buckets):
    sum=0
    for word in keyword:
        sum=sum+ord(word)
    return sum%buckets

print hash_string('Udacity',14)

print hash_string('CS101',20)

print hash_string('abcdefghijklmnop',80)

print hash_string('searchwithpeter.info',73)

print hash_string('udacity',12)
#>>> 11

"""def test_hash_function(func,keys,size):
    results=[0]*size
    keys_used=[]
    for w in keys:
        if w not in keys_used:
            hv=func(w,size)
            results[hv]+=1
            keys_used.append(w)
    return results"""

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

words=get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
print len(words)
counts=test_hash_function(hash_string,words,12)
print counts
