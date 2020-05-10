### making a big index

import time

def time_execution(code): # this procedure gives us the time it takes to evaluate any python expression
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def make_string(p):
    s = ""
    for e in p:
        s = s + e
    return s

def make_big_index(size):
    index = []
    letters = ['a','a','a','a','a','a','a','a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

index1000 = make_big_index(1000)

print time_execution('lookup(index1000, "udacity")')

# output: (None, 8.03e-05)

index10000 = make_big_index(10**4)

print time_execution("lookup(index10000,'udacity')")

# output: (None, 0.0003577999999999637)

index100000 = make_big_index(10**5)

print time_execution("lookup(index100000,'udacity')")

# output: (None, 0.00466710000000603)
