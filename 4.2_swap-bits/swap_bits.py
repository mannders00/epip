
#   0011
# ^ 1010
#   ----
#   1001

def swap_bits(x, i, j):
    ni = (x >> i) & 1
    nj = (x >> j) & 1

    if ni != nj:
        return x ^ ((1 << i) | (1 << j))
    
assert swap_bits(0b1010, 0, 1) == 0b1001
assert swap_bits(0b100101110010010, 4, 6) == 0b100101111000010
