from math import sqrt


def isPrime(l):
    if l % 2 == 0:
        return False
    d = 3
    while d * d <= l and l % d != 0:
        d += 2
        if l % d == 0 and d != l:
            return False
    return True


a = int(input('Enter the any integer number > 2: '))
for i in range(-int(sqrt(a)), -1):
    if a % i == 0 and isPrime(-i):
        print(-i, "- the largest prime factor")
        break
