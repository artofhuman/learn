import itertools


def primes():
    i = 1
    while(True):
        i += 1
        simple = True

        for d in range(2, i):
            if i % d == 0:
                simple = False
                break

        if simple:
            yield i


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
