N, K = map(int, input().split())
A = list(map(int, input().split()))

cs = dict()
# 1: 3, 2: 1, 3: 2, 4: 2, 5: 3, 6:1, 8:1
for i in A:
    cs[i] = cs.get(i, 0) + 1

max_num = max(cs.values())
count = 0
for i, j in cs.items():
    if j >= max_num -1:
        count += 1

print(count)