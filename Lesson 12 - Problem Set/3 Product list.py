# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    i,j=0,1
    while j<=len(list_of_numbers):
        product=list_of_numbers[i]*list_of_numbers[j]
        i=i+1
        j=j+1
    return product

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1
