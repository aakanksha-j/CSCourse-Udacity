# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible
# algorithm or even language of the clear text message, one could perform
# frequency analysis. This process could be described as simply counting
# the number of times a certain symbol occurs in the given text.
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains
# the lowercase letters a-z.
# As output you should return a list of the normalized frequency
# for each of the letters a-z.
# The normalized frequency is simply the number of occurrences, i,
# divided by the total number of characters in the message, n.

def get_count(alphabet,message):

    count=0
    if alphabet in message:
        count=count+1
        #print 'inside get_count:'
        #print count
        endpos=message.find(alphabet)+1
        #print message
    else:
        return 0,0
    #print 'inside get_count 2:',count
    return count,endpos

def get_all_counts(alphabet,message):
    count=0
    while True:
        freq,endpos=get_count(alphabet,message)
        count=count+freq
        if freq:
            message=message[endpos:]
            #print 'inside get_all_counts:'
            #print count
            #print message
        else:
            break
    #print 'return get_all_counts count 2:',count
    return count

def freq_analysis(message):
    #if 'a' in "abcd":
    #    print "abcd".find('a')+1

    alphabetList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w,'x','y','z']
    freq_list=[]
    for i in alphabetList:
        #print 'inside for loop:'
        #print i
        #print message
        #frequency=get_all_counts(i,message)
        #print 'frequency:',frequency
        #equation= frequency*1.0/len(message)
        #print 'equation:',equation
        freq_list.append(get_all_counts(i,message)*1.0/len(message))#equation)
    return freq_list

#Tests

#result= [0.25,0.25,0.25, 0.25, 0.0, ..., 0.0]
#print result==freq_analysis("abcd")


#result= [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]
#print result==freq_analysis("adca")

#print freq_analysis('bewarethebunnies')
result= [0.0625, 0.125, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0625, 0.0625, 0.0, 0.0, 0.0, 0.0, 0.125, 0.0, 0.0, 0.0, 0.0625, 0.0625, 0.0625, 0.0625, 0.0, 0.0, 0.0, 0.0]
print result==freq_analysis('bewarethebunnies')
