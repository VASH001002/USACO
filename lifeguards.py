N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

total_coverage = 0
for x in range(N):
    dih = 0
    interval_temp = intervals.copy()
    interval_temp.pop(x)
    
    for i in range(1000):
        covered = False
        for a, b in interval_temp:
            if a <= i < b:
                covered = True
                break
        if covered:
            dih += 1
    total_coverage = max(total_coverage, dih)


print(total_coverage)