N = int(input())
S = str(input())

sum = 0
for i in range(N):
    A = False
    B = False
    C = False
    if S[i] == "x":
        A = True

    if i > 0:
        if S[i - 1] == "x":
            B = True
    else:
        B = True

    if i < N - 1:
        if S[i + 1] == "x":
            C = True
    else:
        C = True

    if A and B and C:
        sum += 1

print(sum)
