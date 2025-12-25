def main():
    visible = [[False for _ in range(2000)] for _ in range(2000)]

    for i in range(3):
        x1, y1, x2, y2 = map(int, input().split())
        x1 += 1000
        y1 += 1000
        x2 += 1000
        y2 += 1000
        for x in range(x1, x2):
            for y in range(y1, y2):
                visible[x][y] = i < 2

    square_count = 0
    for x in range(2000):
        for y in range(2000):
            square_count += visible[x][y]
    print(square_count)

main()