N = int(input())
seen = dict()
for _ in range(N):
    s = input().lower()
    if s in seen:
        count = seen.get(s)
        seen[s] = count + 1
    else:
        seen[s] = 1

max_count = max(seen.values())
print(max_count)
