N = int(input())
steps = [list(map(int, input().split())) for _ in range(N)]

final = 0

for x in range(1, 4):
    
    location = [0 for _ in range(3)]
    location[x-1] = 1

    current_points = 0
    for step in steps:
        a, b, guess = step
        location[a-1], location[b-1] = location[b-1], location[a-1]

        if location[guess-1]:
            current_points += 1

    final = max(final, current_points)

print(final)
