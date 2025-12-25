N = int(input().strip())
stuff = [tuple(input().split()) for _ in range(N)]
new_list = []

for i in stuff:
    newi = i[2:]
    new_list.append(newi)

main_counter = 0

for i in range(N):
    for j in range(i+1, N):
        dih = 0
        for traits in new_list[i]:
            if traits in new_list[j]:
                dih += 1

        main_counter = max(main_counter, dih)

to_print = main_counter + 1
print(to_print)