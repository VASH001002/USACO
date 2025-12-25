c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

milks = [m1, m2, m3]
caps = [c1, c2, c3]

for i in range(100):
    phase1 = i % 3
    phase2 = (i + 1) % 3

    if milks[phase1] > caps[phase2] - milks[phase2]:
        milks[phase1] -= caps[phase2] - milks[phase2]
        milks[phase2] = caps[phase2]
    else:
        milks[phase2] += milks[phase1]
        milks[phase1] = 0

print(milks[0])
print(milks[1])
print(milks[2])
