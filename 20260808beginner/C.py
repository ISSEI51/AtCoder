from functools import reduce

N, Q = map(int, input().split())

query = [None for _ in range(Q)]
for i in range(Q):
    query[i] = list(map(int, input().split()))

# Q行目のXORを出力する (2,3) -> 2
"""
方針
Nこの数を二進数にした時、各位の1の数をdictにして、2で割ったあまりを保存する -> 10進数に戻した値がQ行目の答え
"""
numbers = [0 for _ in range(N)]
binary_numbers = [None for _ in range(N)]
for i, q in enumerate(query):
    if q[0] == 1:
        numbers[q[1] - 1] += 1
    else:
        # [1,1,2]
        numbers = list(map(lambda x: x - 1 if x > 0 else 0, numbers))
    print(reduce(lambda x, y: x ^ y, numbers))
    """
    # [1,1,11]
    binary_numbers[i] = list(map(lambda x: bin(x)[2:], numbers))
    """
