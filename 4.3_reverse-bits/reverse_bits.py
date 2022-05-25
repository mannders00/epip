
def swap_bits(x, i, j):
    xi = (x >> i) & 1
    xj = (x >> j) & 1
    return x ^ ((1 << i) | (1 << j)) if xi != xj else x

def count_bits(x):
    count = 0
    while x:
        count += 1
        x >>= 1
    return count

def reverse_bits(x):
    bits = count_bits(x)
    for i in range(0, bits // 2):
        x = swap_bits(x, bits // 2 - i - 1, bits // 2 + i + (bits % 2))
    return x

assert swap_bits(0b1100, 0, 3) == 0b0101
assert swap_bits(0b1111, 0, 3) == 0b1111

assert count_bits(0b0000) == 0
assert count_bits(0b1001) == 4
assert count_bits(0b0001) == 1
assert count_bits(0b1000000000) == 10

assert reverse_bits(0b1010) == 0b0101
assert reverse_bits(0b101001) == 0b100101
assert reverse_bits(0b10100) == 0b00101
assert reverse_bits(0b10) == 0b01
assert reverse_bits(0b1100110) == 0b0110011
assert reverse_bits(0b100110) == 0b011001
