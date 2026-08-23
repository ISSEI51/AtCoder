import numpy as np

H, W, K = map(int, input().split())

# 空マスの位置さえ特定できれば算出可能->[(1,2), (4,6)...]
# O(N^2)で解くので候補を落としていく
candidate = np.zeros((H, W))
for i in range(H):
    print(i)
    S = input()
    for j, s in enumerate(S):
        if s == "#":
            candidate[H] = 1
            candidate[:, i] = 1

safe = list(np.where(candidate == 0))
print(safe)
