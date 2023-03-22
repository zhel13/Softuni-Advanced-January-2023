from collections import deque

caffeine = [int(i) for i in input().split(", ")]
energy_drinks = deque(map(int, input().split(", ")))

total_caffeine = 0

while caffeine and energy_drinks:
    amount = caffeine[-1] * energy_drinks[0]
    total_caffeine += amount
    if total_caffeine > 300:
        total_caffeine -= amount
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0
        caffeine.pop()
        energy_drinks.rotate(-1)
    elif total_caffeine <= 300:
        caffeine.pop()
        energy_drinks.popleft()

if energy_drinks:
    print(f"Drinks left: {', '.join([str(s) for s in energy_drinks])}")
    print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
    print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")



