
def to_str(x):
    if x == 0:
        return '0'
    sign = '-' if x < 0 else ''
    x = abs(x)
    temp = ""
    while x:
        temp += str(x % 10)
        x //= 10
    return sign + temp[::-1]

def to_int(s):

    sign = -1 if '-' in s else 1
    s = s.replace('-', '')
    temp = 0
    for c in s:
        temp *= 10
        temp += int(c)
    return sign * temp

assert to_str(0) == '0'
assert to_int('0') == 0
assert to_str(123) == '123'
assert to_int('123') == 123
assert to_str(-123) == '-123'
assert to_int('-123') == -123
