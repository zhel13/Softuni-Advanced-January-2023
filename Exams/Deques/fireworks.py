from collections import deque

effect = deque([int(e) for e in input().split(", ")])
power = deque([int(p) for p in input().split(", ")])

palm_firework_counter = 0
willow_firework_counter = 0
crossette_firework_counter = 0

is_successful_show = False


while True:
    result = 0
    if palm_firework_counter >= 3 and willow_firework_counter >= 3 and crossette_firework_counter >= 3:
        is_successful_show = True
        break
    elif not power or not effect:
        break
    elif effect[0] <= 0:
        effect.popleft()
        continue
    elif power[-1] <= 0:
        power.pop()
        continue
    else:
        result = effect[0] + power[-1]
        if result % 3 == 0 and result % 5 == 0:
            effect.popleft()
            power.pop()
            crossette_firework_counter += 1
        elif result % 3 == 0 and result % 5 != 0:
            effect.popleft()
            power.pop()
            palm_firework_counter += 1
        elif result % 3 != 0 and result % 5 == 0:
            effect.popleft()
            power.pop()
            willow_firework_counter += 1

        else:
            effect[0] -= 1
            effect.rotate(-1)


if is_successful_show:
    print(f"Congrats! You made the perfect firework show!")
    if power:
        print(f"Explosive Power left: {', '.join([str(p) for p in power])}")
    if effect:
        print(f"Firework Effects left: {', '.join([str(p) for p in effect])}")

    print(f"Palm Fireworks: {palm_firework_counter}\n"
          f"Willow Fireworks: {willow_firework_counter}\n"
          f"Crossette Fireworks: {crossette_firework_counter}")
else:
    print(f"Sorry. You can't make the perfect firework show.")
    if power:
        print(f"Explosive Power left: {', '.join([str(p) for p in power])}")
    if effect:
        print(f"Firework Effects left: {', '.join([str(p) for p in effect])}")

    print(f"Palm Fireworks: {palm_firework_counter}\n"
          f"Willow Fireworks: {willow_firework_counter}\n"
          f"Crossette Fireworks: {crossette_firework_counter}")
