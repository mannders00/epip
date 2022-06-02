
def increment(D):
    for i in range(len(D)-1, -1, -1):
        if D[i] == 9:
            D[i] = 0
        else:
            D[i] += 1
            return D

assert increment([5,9,9]) == [6,0,0]
assert increment([5,8,9]) == [5,9,0]
assert increment([2,3,9,8]) == [2,3,9,9]
assert increment([2,3,9,9]) == [2,4,0,0]
