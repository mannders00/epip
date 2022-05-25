
def closest_same_weight(x):
    NUM_BITS = 64
    for i in range(NUM_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            return x ^ ((1 << i) | (1 << (i + 1)))

    raise ValueError('All 1s or 0s')

assert closest_same_weight(6) == 5
assert closest_same_weight(1) == 2
