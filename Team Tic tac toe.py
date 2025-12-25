tictactoe = []
for i in range(3):
    row = []
    x = input()
    for j in range(3):
        row.append(x[j])
    tictactoe.append(row)

possible_combos = []

for i in range(3):
    possible_combos.append([tictactoe[i][0], tictactoe[i][1], tictactoe[i][2]]) #rows
    possible_combos.append([tictactoe[0][i], tictactoe[1][i], tictactoe[2][i]]) #columns

possible_combos.append([tictactoe[0][0], tictactoe[1][1], tictactoe[2][2]]) #diagonal
possible_combos.append([tictactoe[0][2], tictactoe[1][1], tictactoe[2][0]]) #diagonal

solo_count = 0
team_count = 0

for combo in possible_combos:
    combo_set = set(combo)
    if len(combo_set) == 1:
        solo_count += 1
    elif len(combo_set) == 2:
        team_count += 1
print(solo_count)
print(team_count)