# traffic.py
# USACO "Traffic" problem

def clamp0(x):
    return max(0, x)

def intersect(lo, hi, a, b):
    return max(lo, a), min(hi, b)

N = int(input())
segs = []
for _ in range(N):
    kind, a, b = input().split()
    a, b = int(a), int(b)
    segs.append((kind, a, b))

# forward: compute range AFTER mile N
def forward_range():
    lo, hi = -10**15, 10**15
    for kind, a, b in segs:
        if kind == "none":
            lo, hi = intersect(lo, hi, a, b)
        elif kind == "on":
            lo += a
            hi += b
        else:  # off
            lo = clamp0(lo - b)
            hi = clamp0(hi - a)
    return lo, hi

# backward: compute range BEFORE mile 1
def backward_range():
    lo, hi = -10**15, 10**15
    for kind, a, b in reversed(segs):
        if kind == "none":
            lo, hi = intersect(lo, hi, a, b)
        elif kind == "on":
            lo = clamp0(lo - b)
            hi = clamp0(hi - a)
        else:  # off
            lo += a
            hi += b
    return lo, hi

init_lo, init_hi = backward_range()
final_lo, final_hi = forward_range()

print(init_lo, init_hi)
print(final_lo, final_hi)
