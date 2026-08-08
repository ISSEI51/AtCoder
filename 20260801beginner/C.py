N = int(input())
S = str(input())

hit_index = set()  # {0,2,4}
for j in range(N - 1):
    if S[j] == "o":
        hit_index.add(j)


for k in range(1, N + 1):
    # 先頭からk袋取ることを考える
    # 2poointerで考える
    # left, rightはそれぞれインデックス
    # 毎回leftを0から始めるのは非効率!!
    o_num = 0
    for l in range(k):
        if S[l] == "o":
            o_num += 1

    left = k - 1
    right = k + o_num - 1

    while left <= right:
        recieve = 0

        current_range = set(range(left, right + 1))
        recieve = len(current_range & hit_index) - o_num

        left = right + 1
        right = right + recieve

        if right > N - 1:
            right = N - 1
            break

    eatable = right + 1  # インデックスを個数に戻す
    print(eatable)
