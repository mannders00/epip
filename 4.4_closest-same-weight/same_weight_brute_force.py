
def weight(x):
    c = 0
    while x:
        c += 1
        x = x&(x-1)
    return c

def closest_same_weight(x):
    y = 1
    while True:
        if weight(x + y) == weight(x):
            return x + y
        elif weight(x - y) == weight(x):
            return x - y
        else:
            y += 1

assert closest_same_weight(6) == 5
assert closest_same_weight(1) == 2
