# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000.0 # km per second

def speed_fraction(time_in_ms, distance):
    return 2 * distance / ((time_in_ms / 1000.0) * speed_of_light)


print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?

# ZeroDivisionError: float division by zero
# used 1000.0 for float division to avoid rounding off to 0 and giving error
