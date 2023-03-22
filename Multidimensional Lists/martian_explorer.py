def resources(current_pos, status_resources):
    if current_pos == "W":
        print(f"Water deposit found at {tuple(map(int, rover_position))}")
        status_resources[0] = True
    elif current_pos == "C":
        print(f"Concrete deposit found at {tuple(map(int, rover_position))}")
        status_resources[1] = True
    elif current_pos == "M":
        print(f"Metal deposit found at {tuple(map(int, rover_position))}")
        status_resources[2] = True


SIZE = 6
matrix = []
all_resources = [False, False, False]
rover_position = []

for row in range(SIZE):
    line = input().split()
    matrix.append(line)
    if "E" in line:
        rover_position = [row, line.index("E")]

directions = input().split(", ")

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1),
}

while directions:
    r = rover_position[0] + direction[directions[0]][0]
    c = rover_position[1] + direction[directions[0]][1]

    if r < 0:
        r = SIZE - 1
    elif c < 0:
        c = SIZE - 1
    elif r == SIZE:
        r = 0
    elif c == SIZE:
        c = 0
    rover_position = [r, c]
    current_position = matrix[r][c]

    if current_position != "R":
        resources(current_position, all_resources)
    else:
        print(f"Rover got broken at {tuple(map(int, rover_position))}")
        break
    directions.pop(0)

if all(all_resources):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
