from random import random
from math import log

ALPHA = 1
BETA = 1

def generate_time(x, const):
    return -const * log(1-x)

time_arrival = 0
time_service = 0
clock = 0
queue = 1

while clock < 10:
    # Checks whether a service or arrival will happen first.
    if time_arrival < time_service:
        # Subtracts passed time.
        time_service -= time_arrival
        # Counts up clock.
        clock += time_arrival
        # Adds to queue.
        queue += 1

        # Generates new arrival time.
        x = random()
        time_arrival = generate_time(x, ALPHA)

    else:
        # Subtracts passed time.
        time_arrival -= time_service
        # Counts up clock.
        clock += time_service
        # Adds to queue.
        queue -= 1

        # Generates new service time.
        x = random()
        time_service = generate_time(x, BETA)

    # If queue is empty, skip to next arrival.
    if queue == 0:
        # Counts up clock.
        clock += time_arrival
        # Adds to queue.
        queue += 1

        # Generates new arrival time.
        x = random()
        time_arrival = generate_time(x, ALPHA)

