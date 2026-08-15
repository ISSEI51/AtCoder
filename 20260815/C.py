N = int(input())
A = list(map(int, input().split()))

left = 0
right = 0
hit = 0
distance = 0
latest_hit = 0
nums = set(A)
# nums = {-11,-4,-1,2}
# -1 -4 2 -11 -> 1 4 10 23
while hit < N:
    left -= 1
    right += 1
    if left in nums:
        hit += 1
        if latest_hit < 0:
            distance += abs(left - latest_hit)
        else:
            distance += latest_hit + abs(left)
        latest_hit = left
        right = left
        nums.remove(left)
    elif right in nums:
        hit += 1
        if latest_hit < 0:
            distance += abs(latest_hit) + right
        else:
            distance += right - latest_hit
        latest_hit = right
        left = right
        nums.remove(right)
    else:
        continue

    # print(f"left: {left}, right: {right} dist: {distance}")

print(distance)
