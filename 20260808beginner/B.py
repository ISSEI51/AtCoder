N = int(input())
C = list(map(int, input().split()))

seen = dict()
for c in C:
    seen[c] = seen.get(c, 0) + 1

max_c = 0
for c, num in seen.items():
    if num > max_c:
        max_c = num
        pick_c = c

del seen[pick_c]

count = 0
for num in seen.values():
    count += num

print(count)
