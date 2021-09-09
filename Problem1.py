sum, a, b, MAX = 0, 1, 2, 4000000
while b < MAX:
    if b % 2 == 0:
        sum += b
    a, b = b, a + b
print(sum)
