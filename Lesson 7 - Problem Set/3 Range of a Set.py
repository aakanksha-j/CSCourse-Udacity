# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(n1,n2,n3):
    if n1>n2:
        big,bigger=n2,n1
        if n1>n3:
            bigger,biggest=n3,n1
        else:
            bigger,biggest=n1,n3
    else:
        big,bigger=n1,n2
        if n2>n3:
            bigger,biggest=n3,n2
        else:
            bigger,biggest=n2,n3

    return biggest-big
    # Your code here


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6
