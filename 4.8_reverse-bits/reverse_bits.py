
def reverse(x):
    result, rem = 0, abs(x)

    while rem:
        result *= 10
        result += rem % 10
        rem = rem // 10

    return -result if x < 0 else result

assert reverse(12345) == 54321
assert reverse(-12345) == -54321
assert reverse(0) == 0
assert reverse(-1) == -1
assert reverse(-100) == -1
assert reverse(500) == 5
assert reverse(590) == 95
