Q = int(input())
S = input()
T = input()
query = [list(map(int, input().split())) for _ in range(Q)]

"""
T = "abc"
S = "ababc"
S_dict = {"a": [0,2], "b": [1,3], "c": [4]}
-> {"a": [0,2], "b": [0,2], "c": [3]}
-> No
"""
S_dict = dict.fromkeys(T, set())
for i, c in enumerate(S):
    if c in S_dict:
        S_dict[c].add(i)

print(S_dict)

count = 0
for k, v in S_dict.items():
    v = map(lambda x: x-count, v)
    count += 1

# マッチする先頭のTのインデックスが決定する 
match_index = S_dict[T[0]]
for k, v in S_dict.items():
    match_index = match_index & v

print(match_index)

for q in query:
    L = q[0]-1
    R = q[1]-1
    if R-L+1 < len(T):
        print("No")
        continue
    match_start_range = set(range(L, R-len(T)+1))
    print(match_start_range)
    print("Yes" if match_index & match_start_range else "No")