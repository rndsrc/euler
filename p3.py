from math import sqrt

v = 600851475143
n = int(sqrt(v))

def isprime(i):
    pass

for i in range(2, n+1):
    if isprime(i):
        if v % n == 0:
            print(v / n)
            break
