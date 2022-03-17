s = 0
l = 1
n = 1

while n <= 4_000_000:
    if n % 2 == 0:
        s += n
    l, n = n, l + n

print(s)
