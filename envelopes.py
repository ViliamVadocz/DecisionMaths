import sys
import random
import matplotlib.pyplot as plt

MAX = sys.maxsize
ATTEMPTS = 1000
ENVELOPES = 100

def get_envelopes():
    return [int(random.randint(0, MAX)) for _ in range(ENVELOPES)]

def play(envelopes, open_before_try_largest):
    largest_so_far = -1
    for i, elem in enumerate(envelopes):
        if i < open_before_try_largest:
            if elem > largest_so_far:
                largest_so_far = elem
        elif elem > largest_so_far:
            picked = elem
            break
    else:
        picked = envelopes[-1]
    return picked == max(envelopes)

wins = {i: sum(play(get_envelopes(), i) for _ in range(ATTEMPTS)) for i in range(ENVELOPES)}

plt.plot([*wins.keys()], [*wins.values()])
plt.show()
