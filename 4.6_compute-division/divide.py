
def divide(x, y):
    quot, pow = 0, 32
    y_pow = y << pow

    while x >= y:
        while y_pow > x:
            pow -= 1
            y_pow >>= 1
        
        quot += 1 << pow
        x -= y_pow
    return quot

assert divide(494,321) == 494//321
assert divide(3208932,38273) == 3208932//38273
