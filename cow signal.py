signal_list = []
M, N, K = map(int, input().split())
for x in range(M):
    signal_list.append(input())

for signal in signal_list:
    current = ""
    for x in signal:
        for i in range(K):
            current += x
    for z in range(K):
      print(current)

