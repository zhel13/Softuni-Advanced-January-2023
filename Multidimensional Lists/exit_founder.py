players = input().split(", ")

size = 6
matrix = []
players_status = [True, True]

for _ in range(size):
    line = input().split()
    matrix.append(line)

player_num = 1

while True:
    coordinates = input()
    player_turn_index = 1 if player_num % 2 == 0 else 0
    player_turn = players[player_turn_index]

    r_string = coordinates.replace("(", "").replace(")", "").split(", ")[0]
    c_string = coordinates.replace("(", "").replace(")", "").split(", ")[1]
    r, c = int(r_string), int(c_string)
    position = matrix[r][c]
    if players_status[player_turn_index]:
        if position == "W":
            print(f"{player_turn} hits a wall and needs to rest.")
            players_status[player_turn_index] = False

        elif position == "E":
            print(f"{player_turn} found the Exit and wins the game!")
            break
        elif position == "T":
            if player_turn == players[0]:
                winner = players[1]
            else:
                winner = players[0]
            print(f"{player_turn} is out of the game! The winner is {winner}.")
            break

    else:
        players_status[player_turn_index] = True
    player_num += 1










