import random


def is_sorted(arr):
    size = len(arr)
    if size < 2:
        return True
    for i in range(1, size):
        if arr[i - 1] > arr[i]:
            return False
    return True


def random_integers(max, size):
    for _ in range(size):
        yield random.randint(0, max)