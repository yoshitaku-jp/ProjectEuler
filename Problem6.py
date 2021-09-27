ans1 = 0
for i in range(1, 101):
    ans1 += i ** 2
print(ans1)

ans2 = 0
for i in range(1, 101):
    ans2 += i
ans2 = ans2 ** 2
print(ans2)

print(ans2 - ans1)
