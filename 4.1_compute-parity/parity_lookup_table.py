# Generate parity map with brute force algorithm
# this is bad performance on first execution but
# about 4x better in the long run.

import parity_iterate

parity_map = {}
mask_size = 16
BIT_MASK = 0xFFFF

for i in range(2 ** mask_size):
    parity_map[i] = parity_iterate.parity(i)

def parity(x):
    return  parity_map[x & BIT_MASK] ^ \
            parity_map[((x >> (1 * mask_size))) & BIT_MASK] ^ \
            parity_map[((x >> (2 * mask_size))) & BIT_MASK] ^ \
            parity_map[((x >> (3 * mask_size))) & BIT_MASK]

assert parity(0b1011) == 1
assert parity(0b1111) == 0
assert parity(0b10001000) == 0
