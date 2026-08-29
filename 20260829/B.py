N = int(input())
A = list(map(int, input().split()))

seen = set()
count = 0
for i in A:
    if i in seen:
        seen.remove(i)
        count -= i
    else:
        seen.add(i)
        count += i
print(count)