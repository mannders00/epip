
def parity(x):
    bits = 0
    while x:
        bits += 1 if x & 1 else 0
        x >>= 1
    return 0 if bits % 2 == 0 else 1

assert parity(0b1011) == 1
assert parity(0b10001000) == 0
