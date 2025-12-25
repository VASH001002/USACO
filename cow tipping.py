n = int(input())
cows = []
for _ in range(n):
    cows.append(list(input().strip())) 
ans = 0
for i in range(n):
    for j in range(n):
        if cows[2-i][2-j] == "1":
            for k in range(n):
                for l in range(n):
                    if k <= i and l <= j:
                        if cows[k][l] == "0":
                            cows[k][l] = "1"   
                        else:
                            cows[k][l] = "0"
            ans += 1

print(ans)
