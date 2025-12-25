x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

area = (x2-x1) * (y2-y1)

if min(x2, x4) > max(x1, x3) and min(y2, y4) > max(y1, y3):
    area -= (min(x2, x4) - max(x1, x3)) * (min(y2, y4) - max(y1, y3))

if min(x2, x6) > max(x1, x5) and min(y2, y6) > max(y1, y5):
    area -= (min(x2, x6) - max(x1, x5)) * (min(y2, y6) - max(y1, y5))

if min(x4, x6) > max(x3, x5) and min(y4, y6) > max(y3, y5):
    x1overlap = max(x3, x5)
    y1overlap = max(y3, y5)
    x2overlap = min(x4, x6)
    y2overlap = min(y4, y6)

    if min(x2overlap, x2) > max(x1overlap, x1) and min(y2overlap, y2) > max(y1overlap, y1):
        area += (min(x2overlap, x2) - max(x1overlap, x1)) * (min(y2overlap, y2) - max(y1overlap, y1))

if area <= 0:
    print("NO")
else:
    print("YES")
