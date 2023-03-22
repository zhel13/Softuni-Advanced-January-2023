from collections import deque

seats = input().split(", ")
first_number = deque([int(x) for x in input().split(", ")])
second_number = deque([int(x) for x in input().split(", ")])

rotations = 0
seat_matches = 0
seat_match = []

while True:
    if rotations == 10 or seat_matches == 3:
        break
    else:
        check_char = chr(first_number[0] + second_number[-1])
        result1 = str(first_number[0])+check_char
        result2 = str(second_number[-1])+check_char

        if result1 in seats or result2 in seats:
            if result1 in seat_match or result2 in seat_match:
                first_number.popleft()
                second_number.pop()
            else:
                first_number.popleft()
                second_number.pop()
                seat_matches += 1
                if result1 in seats:
                    seat_match.append(result1)
                else:
                    seat_match.append(result2)
        else:
            first_number.rotate(-1)
            second_number.rotate(1)
        rotations += 1
print(f"Seat matches: {', '.join(seat_match)}")
print(f"Rotations count: {rotations}")
