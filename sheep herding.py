positions = list(map(int, input().split()))
positions.sort()

a, b, c = positions
gap1 = b - a - 1
gap2 = c - b - 1

# Compute minimum moves
if gap1 == 0 and gap2 == 0:
    min_moves = 0
elif gap1 == 1 or gap2 == 1:
    min_moves = 1
else:
    min_moves = 2

# Maximum moves
max_moves = max(gap1, gap2)

print(min_moves)
print(max_moves)
