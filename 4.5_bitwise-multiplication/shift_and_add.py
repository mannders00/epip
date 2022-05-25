

def multiply(x, y):

    def add_rec(a,b):
        if not a:
            return b
        else:
            return add_rec((a & b) << 1, a ^ b)

    running_sum = 0
    while x:
        if x & 1:
            running_sum = add_rec(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

assert multiply(0, 0) == 0 * 0
assert multiply(6, 8) == 6 * 8
assert multiply(3289, 4783) == 3289 * 4783
