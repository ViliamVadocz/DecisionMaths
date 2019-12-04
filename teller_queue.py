from random import random
from math import log

# TODO
# - average waiting times               [ ]
# - maximum waiting times               [ ]
# - average queue lengths               [X]
# - maximum queue lengths               [X]
# - total idle time for teller          [X]

# Average interarrival time.
ALPHA = 120 
# Average service time.
BETA = 60

def generate_time(x, const):
    return -const * log(1-x)

time_arrival = 0
time_service = 0
clock = 0
queue = 1
max_queue = 1
collective_queue_time = 0
teller_idle = 0

# Simulating 8 hour day.
while clock < 8*60*60:
    # Checks whether a service or arrival will happen first.
    if time_arrival < time_service:
        # Subtracts passed time.
        time_service -= time_arrival
        # Counts up clock.
        clock += time_arrival
        # Adds to collective time spent in queue.
        collective_queue_time += queue * time_arrival
        # Adds to queue.
        queue += 1

        # Tracks maximum queue length.
        if queue > max_queue: max_queue = queue

        # Generates new arrival time.
        x = random()
        time_arrival = generate_time(x, ALPHA)

    else:
        # Subtracts passed time.
        time_arrival -= time_service
        # Counts up clock.
        clock += time_service
        # Adds to collective time spent in queue.
        collective_queue_time += queue * time_service
        # Adds to queue.
        queue -= 1

        # Generates new service time.
        x = random()
        time_service = generate_time(x, BETA)

    # If queue is empty, skip to next arrival.
    if queue == 0:
        # Counts up clock.
        clock += time_arrival
        # Counts up teller idle time.
        teller_idle += time_arrival
        # Adds to queue.
        queue += 1

        # Generates new arrival time.
        x = random()
        time_arrival = generate_time(x, ALPHA)

# Print statistics.
print(f'Total simulated time: {clock}')

average_queue_len = collective_queue_time / clock
print(f'Average queue length: {average_queue_len}')
print(f'Maximum queue length: {max_queue}')