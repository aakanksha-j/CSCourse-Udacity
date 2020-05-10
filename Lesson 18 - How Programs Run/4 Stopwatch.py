import time

def time_execution(code): # this procedure gives us the time it takes to evaluate any python expression
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i<n:
        i = i+1

#print time_execution('1 + 1') # In python shell, only write time_execution(expression) and 2 variables in return statement will be returned.
print time_execution('spin_loop(10**9)')[1]
