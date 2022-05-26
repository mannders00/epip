import math

def is_palindrome(x):
    if x < 0:
        return False

    length = math.floor(math.log(x, 10)) + 1
    msd_mask = 10 ** (length - 1)

    for _ in range(length // 2):
        if x // msd_mask != x % 10:
            return False

        x %= 10
        x //= 10
        msd_mask //= 100

    return True

assert is_palindrome(123454321) == True
assert is_palindrome(12) == False
assert is_palindrome(121) == True
assert is_palindrome(-121) == False
