# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7] # spy is a list
a=3 # a is a string
def replace_spy(spy,a):
    spy[2]=spy[2]+1
    a=a+3
    return spy,a

# In the test below, the first line calls your
# procedure which will change spy, and the
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy,a)
print spy,a
#>>> [0,0,8],3
