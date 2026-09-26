N, D = map(int, input().split())
X = list(map(int, input().split()))

"""
D = 3
4 77 20 26 9 26 22 40
sorted X = [9, 20, 22, 26, 26, 40, 77]
"""

X_sorted = sorted(X)
count = 0
ans_value = set()
for k, v in enumerate(X_sorted):
    if k == 0:
        if v + D <= X_sorted[k+1]:
            count += 1
            ans_value.add(v)
            continue
    elif k == N-1:
        if v - D >= X_sorted[k-1]:
            count += 1
            ans_value.add(v)
            continue
    else:
        if v - D >= X_sorted[k-1] and v + D <= X_sorted[k+1]:
            count += 1
            ans_value.add(v)
            continue

print(count)
ans_idnex = []
for k, v in enumerate(X):
    if v in ans_value:
        ans_idnex.append(k+1)
print(*ans_idnex)