
from reverse_bits import reverse_bits

d = {}
for i in range(0, 0xFFFF + 1):
    d[i] = reverse_bits(i)

def reverse_bits_lookup(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return  d[ (x >> (MASK_SIZE * 0)) & BIT_MASK] << (MASK_SIZE * 3) | \
            d[ (x >> (MASK_SIZE * 1)) & BIT_MASK] << (MASK_SIZE * 2) | \
            d[ (x >> (MASK_SIZE * 2)) & BIT_MASK] << (MASK_SIZE * 1) | \
            d[ (x >> (MASK_SIZE * 3)) & BIT_MASK] << (MASK_SIZE * 0)

assert reverse_bits_lookup(0xFFFF0000FFFF0000) == 0xFFFF0000FFFF
