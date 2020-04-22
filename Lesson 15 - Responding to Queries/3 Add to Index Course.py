# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index1 = []

def add_to_index(index1,keyword,url):
    for entry in index1:
        if entry[0]==keyword:
            entry[1].append(url)
            return
    index1.append([keyword,[url]])

add_to_index(index1,'udacity','http://udacity.com')
add_to_index(index1,'computing','http://acm.org')
add_to_index(index1,'udacity','http://npr.org')
print index1
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]
