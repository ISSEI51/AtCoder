import math

N = int(input())
A = list(map(int, input().split()))

m = math.ceil(N/2)

ans = 0
for i in range(m,N):
    ans += A[i]


print(ans)