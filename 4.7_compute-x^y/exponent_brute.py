
def exponent(x, y):
    result = x
    for _ in range(y-1):
        result *= x
    return result


assert(exponent(4,4)) == 4 ** 4
assert(exponent(4,16)) == 4 ** 16
