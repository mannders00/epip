
def exponent(x,y):
    if y == 0:
        return 1

    exp = exponent(x, y // 2)
    if y & 1:
        return x * (exp * exp)
    else:
        return exp * exp

print(exponent(9,3))
#assert exponent(9,2) == 9 ** 2
#assert exponent(9.5,2) == 9.5 ** 2
#assert exponent(100,4) == 100 ** 3
