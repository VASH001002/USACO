N = int(input())
rooms = [int(input()) for _ in range(N)]

final = 100000000

for y in range(len(rooms)):
    thing = 0 
    for x in range(len(rooms)):
        thing += rooms[x] * ((x-y) % N)
    final = min(final, thing)

print(final)
