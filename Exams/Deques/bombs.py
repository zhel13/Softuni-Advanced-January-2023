from collections import deque

DATURA = 40
CHERRY = 60
SMOKEDECOY = 120

bomb_effect = deque([int(x) for x in input().split(", ")])
bomb_casing = [int(x) for x in input().split(", ")]

datura_bomb = 0
cherry_bomb = 0
smoke_decoy_bomb = 0

success = [False, False, False]

while bomb_effect or bomb_casing:
    if all(success):
        break
    else:
        result = bomb_effect[0] + bomb_casing[-1]
        if result == DATURA or result == CHERRY or result == SMOKEDECOY:
            if result == DATURA:
                datura_bomb += 1

            elif result == CHERRY:
                cherry_bomb += 1

            elif result == SMOKEDECOY:
                smoke_decoy_bomb += 1
            bomb_effect.popleft()
            bomb_casing.pop()
        else:
            bomb_casing[-1] -= 5

        if datura_bomb == 3:
            success[0] = True
            continue
        elif cherry_bomb == 3:
            success[1] = True
        elif smoke_decoy_bomb == 3:
            success[2] = True


if all(success):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(x)for x in bomb_effect)}")
else:
    print(f"Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(x)for x in bomb_casing)}")
else:
    print("Bomb Casings: empty")


print(f"Cherry Bombs: {cherry_bomb}\nDatura Bombs: {datura_bomb}\nSmoke Decoy Bombs: {smoke_decoy_bomb}")
