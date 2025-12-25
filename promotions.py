a1, a2 = map(int, input().strip().split())
b1, b2 = map(int, input().strip().split())
c1, c2 = map(int, input().strip().split())
d1, d2 = map(int, input().strip().split())

ans1 = (d2 + c2 + b2) - (d1 + c1 + b1)
ans2 = (d2 + c2) - (d1 + c1)
ans3 = d2 - d1

print(ans1)
print(ans2)
print(ans3)
