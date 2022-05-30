
import random, pprint

def randint(a, b):

    def zero_one_random():
        return int(random.randint(0, 1))

    outcomes = b - a
    while True:
        i, result = 0, 0
        while (1 << i) < outcomes:
            result = (result << 1) | zero_one_random()
            i += 1

        if result < outcomes:
            return a + result


results = {}
for i in range(0, 1000):
    num = randint(0, 10)
    if num not in results:
        results[num] = 1
    else:
        results[num] += 1

# Amount of times certain number was picked should be roughly the same
print(results)
