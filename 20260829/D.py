N, K = map(int, input().split())

# 1*i + 2*j + 3*k = K -> (i,j,k)

# nと引いた回数を記録
a = dict()
for i in reversed(range(1, N+1)):
    max_num = K//i
    for j in range(1,max_num+1):
        a[K-i*j] = a.get(K-i*j,[0]*N)[i-1] + 1
