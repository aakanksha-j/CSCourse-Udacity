# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

def splitlist_conversion_to_list(splitlist):
    separatorList=[]
    for e in splitlist:
        separatorList.append(e)
    return separatorList

def split_string(source,splitlist):
    lastWord=''
    outputList=[]
    separatorList=splitlist_conversion_to_list(splitlist)
    for e in source:
        if e in separatorList:
            if lastWord:
                outputList.append(lastWord)
            lastWord=''
        else:
            lastWord=lastWord+e
            if len(source)==1:
                outputList.append(lastWord)
        source=source[source.find(e)+1:]
    return outputList

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']---

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
