size = int(input())
car_number = input()

matrix = []
tunel_position = []
car_position = [0, 0]
km_reached = 0
has_won = True

for row in range(size):
    line = input().split()
    matrix.append(line)

for r_i in range(len(matrix)):
    for c_i in range(len(matrix)):
        if matrix[r_i][c_i] == "T":
            pos = [r_i, c_i]
            tunel_position.append(pos)

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1),
}

directions = input()

while directions != "End":

    r = car_position[0] + direction[directions][0]
    c = car_position[1] + direction[directions][1]

    # if not (0 <= r < size and 0 <= c < size):
    #     break
    car_position = [r, c]
    position = matrix[r][c]
    if position != "T":
        km_reached += 10
    elif position == "T":
        matrix[r][c] = "."
        r = tunel_position[1][0]
        c = tunel_position[1][1]
        car_position = [r, c]
        matrix[r][c] = "."
        km_reached += 30

    if position == "F":
        has_won = True
        break
    else:
        has_won = False

    directions = input()
matrix[car_position[0]][car_position[1]] = "C"
if not has_won:

    print(f"Racing car {car_number} DNF.")
    print(f"Distance covered {km_reached} km.")

elif has_won:
    print(f"Racing car {car_number} finished the stage!")
    print(f"Distance covered {km_reached} km.")

for ch in matrix:
    print("".join(ch))
