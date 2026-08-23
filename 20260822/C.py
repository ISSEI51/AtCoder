N, M, K = map(int, input().split())
A = list(map(int, input().split()))

# 4,5,7,3,1,43,754...
cal = 0
# ate_days = set()
is_ate = dict()
for i in range(N):
    # print(f"---------{i}-----------")
    """
    eate_rage = set(range(max(i - M + 1, 0), i + 1))
    if len(list(ate_days - eate_rage)):
        out = int(list(ate_days - eate_rage)[0])
        cal = cal - A[out]
        ate_days.remove(out)
    """
    try:
        if is_ate[i - M] == "Yse":
            cal -= A[i - M]
    except:
        pass

    if cal + A[i] <= K:
        print("Yes")
        cal += A[i]
        # ate_days.add(i)
        is_ate[i] = "Yse"

    else:
        print("No")
        is_ate[i] = "No"
