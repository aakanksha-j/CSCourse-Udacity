# How long does the data spend at hte routers?

# Information given in question

total_time = 75 # milliseconds trancroute, round trip Birmingham -> Sundsvall
one_way_distance = 2500 # km, Birmingham -> Sundsvall
optic_speed = 200000 # km/s
ms_per_second = 1000 # conversion from ms to seconds (ms/sec)

# Calculations

time_on_the_wires = 2.0 * one_way_distance / optic_speed * ms_per_second # [km] / [km/s] * [ms/s]
print time_on_the_wires

total_time_at_routers = total_time - time_on_the_wires
print total_time_at_routers
