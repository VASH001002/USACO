import itertools

s = input()
perms = set(itertools.permutations(s))
print(len(set(perms)))

for perm in perms:
    print(''.join(perm))