distance = 4300*2 # km between Palo Alto and Cambridge
c = 300000.0 # km/s ( approximate speed of light)
time = 0.1 # 100ms = .1s

light_time = distance/c  # 0.02867seconds or 28.67milliseconds is time taken by light to travel that distance

print light_time
print time/light_time # data is taking 3.5 times longer than light to travel in vacuum

# If you had vacuum between two points and then sent data, you could have sent it 3.5 times faster.
