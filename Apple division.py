result = float('inf')
total = 0

def completeSearch(weights, i, N, currentSum):
    global result, total
    if i == N:
        result = min(result, abs(total - 2 * currentSum))
    else:
        completeSearch(weights, i + 1, N, currentSum)

        completeSearch(weights, i + 1, N, currentSum+weights[i])

N = int(input())
weights = list(map(int, input().split()))
total = sum(weights)
completeSearch(weights, 0, N, 0)
print(result)