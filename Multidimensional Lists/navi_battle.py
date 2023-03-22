# size = int(input())
#
# matrix = []
# marine_pos = []
#
# ships_count = 0
# mines_count = 0
#
# has_won = False
# for row in range(size):
#     line = input()
#     matrix.append(list(line))
#     if "S" in line:
#         marine_pos = [row, line.index("S")]
#         matrix[row][marine_pos[1]] = "-"
#
# direction = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, - 1),
#     "right": (0, 1),
# }
#
# while True:
#     if ships_count == 3:
#         has_won = True
#         break
#     elif mines_count == 3:
#         has_won = False
#         break
#     else:
#         directions = input()
#
#         r = marine_pos[0] + direction[directions][0]
#         c = marine_pos[1] + direction[directions][1]
#
#         if not (0 <= r < size and 0 <= c < size):
#             break
#         else:
#             marine_pos = [r, c]
#             position = matrix[r][c]
#
#             if position == "C":
#                 ships_count += 1
#                 matrix[r][c] = "-"
#             elif position == "*":
#                 mines_count += 1
#                 matrix[r][c] = "-"
#
# if has_won:
#     matrix[r][c] = "S"
#     print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#     [print("".join(rows)) for rows in matrix]
# if not has_won:
#     matrix[r][c] = "S"
#     print(f"Mission failed, U-9 disappeared! Last known coordinates {marine_pos}!")
#     [print("".join(rows)) for rows in matrix]


size = int(input())

matrix = []
marine_pos = []

ships_count = 3
mines_count = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1),

}

for row in range(size):
    line = list(input())
    matrix.append(line)
    if "S" in line:
        marine_pos = [row, line.index("S")]
        matrix[row][marine_pos[1]] = "-"

while ships_count:
    direction = input()

    r = directions[direction][0] + marine_pos[0]
    c = directions[direction][1] + marine_pos[1]

    marine_pos = [r, c]

    if matrix[r][c] == "C":
        ships_count -= 1
    elif matrix[r][c] == "*":
        mines_count += 1

        if mines_count == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates {marine_pos}!")
            break

    matrix[r][c] = "-"
else:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

matrix[marine_pos[0]][marine_pos[1]] = "S"
[print(*row, sep="") for row in matrix]
