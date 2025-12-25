n, m = map(int, input().split())

speedLimits = []
for _ in range(n):
    length, limit = map(int, input().split())
    for _ in range(length):
        speedLimits.append(limit)

bessieSpeeds = []
for _ in range(m):
    length, speed = map(int, input().split())
    for _ in range(length):
        bessieSpeeds.append(speed)

max_over = 0
for i in range(100):
    max_over = max(max_over, bessieSpeeds[i] - speedLimits[i])

print(max_over)
