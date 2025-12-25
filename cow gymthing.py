K, N = map(int, input().split())
performances = [list(map(int, input().split())) for _ in range(K)]

count = 0

# check all pairs of cows (a, b)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        a, b = i + 1, j + 1  # cow numbers (1..N)
        consistent = True
        
        # check if a is always ranked higher than b
        for k in range(K):
            if performances[k].index(a) > performances[k].index(b):
                consistent = False
                break
        
        if consistent:
            count += 1

print(count)




