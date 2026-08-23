N = int(input())
L = list(map(int, input().split()))

left = 0
right = N - 1

l_length = L[0]
r_length = L[N - 1]

while left < right - 1:
    if l_length <= r_length:
        left += 1
        l_length += L[left]

    else:
        right -= 1
        r_length += L[right]

print(abs(l_length - r_length))
