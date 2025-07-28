import time
import random
from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort

def generate_data(size, data_type):
    if data_type == 'random':
        return random.sample(range(size * 10), size)
    elif data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reverse':
        return list(range(size, 0, -1))

sizes = [1000, 5000, 10000]
distributions = ['random', 'sorted', 'reverse']

for size in sizes:
    for dist in distributions:
        data = generate_data(size, dist)
        data_copy = data[:]

        start = time.time()
        quicksort(data)
        end = time.time()
        print(f"Deterministic | Size: {size}, Dist: {dist}, Time: {end - start:.5f}s")

        start = time.time()
        randomized_quicksort(data_copy)
        end = time.time()
        print(f"Randomized    | Size: {size}, Dist: {dist}, Time: {end - start:.5f}s\n")
