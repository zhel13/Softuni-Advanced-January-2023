size = int(input())

matrix = []
player_position = []
position_matrix = []

coins_count = 0
has_won = True

for row in range(size):
    line = input().split()
    matrix.append(line)
    if "P" in line:
        player_position = [row, line.index("P")]
        matrix[row][player_position[1]] = "0"
        position_matrix.append(player_position)


direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1),
}

while coins_count < 100:
    directions = input()
    r = player_position[0] + direction[directions][0]
    c = player_position[1] + direction[directions][1]

    if r < 0:
        r = size - 1
    elif c < 0:
        c = size - 1
    elif r == size:
        r = 0
    elif c == size:
        c = 0

    player_position = [r, c]
    position = matrix[r][c]
    position_matrix.append(player_position)
    if position == "X":
        coins_count //= 2
        has_won = False
        break
    elif position.isdigit():
        coins_count += int(position)
        matrix[r][c] = '0'

if has_won:
    print(f"You won! You've collected {coins_count} coins.")
    print("Your path:")

else:
    print(f"Game over! You've collected {coins_count} coins.")
    print("Your path:")
for position in position_matrix:
    print(position)
