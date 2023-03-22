from collections import deque

males = deque([int(m) for m in input().split(" ")])
females = deque([int(f) for f in input().split(" ")])
match_counter = 0

while females and males:
    if females[0] <= 0 or males[-1] <= 0:
        if females[0] <= 0:
            females.popleft()
        else:
            males.pop()
    elif females[0] > 0 and males[-1] > 0:
        if females[0] != males[-1]:
            females.popleft()
            males[-1] -= 2
        else:
            if females[0] % 25 == 0 or males[-1] % 25 == 0:
                if females[0] % 25 == 0:
                    females.popleft()
                    females.popleft()
                else:
                    males.pop()
                    males.pop()
            else:
                females.popleft()
                males.pop()
                match_counter += 1


print(f"Matches: {match_counter}")
if males:
    print(f"Males left: {', '.join(str(males[m]) for m in range(len(males)-1,-1,-1))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(f) for f in females])}")
else:
    print("Females left: none")
