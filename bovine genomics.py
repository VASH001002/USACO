N, M = map(int, input().strip().split())
grid = [input().strip() for _ in range(2 * N)]

def counting_stuff(grid):
    count = 0
    # loop through columns
    for x in range(M):
        valid = True
        # loop through each spotty cow
        for y in range(N):
            # compare with each plain cow
            for z in range(N):
                if grid[y][x] == grid[z + N][x]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            count += 1
    return count

print(counting_stuff(grid))
