ans = []

for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        result = str(a * b)
        if result == result[::-1]:
            ans.append(int(result))

print((max(ans)))
