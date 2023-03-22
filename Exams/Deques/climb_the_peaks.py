from collections import deque
import sys
from io import StringIO

test_input1 = '''40, 40, 40, 40, 40, 40, 40
40, 50, 60, 20, 30, 5, 2
'''

test_input2 = '''10, 20, 34, 26, 12, 10, 45
30, 28, 17, 17, 13, 10, 10
'''

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def adding_peaks():
    food_value = food_portion.pop()
    stamina_value = stamina.popleft()
    total_value = food_value + stamina_value

    for climbed, value in peaks.items():
        if total_value < value:
            return

        elif total_value >= value and climbed in climbed_peaks:
            continue

        elif total_value >= value and climbed not in climbed_peaks:
            climbed_peaks[climbed] = value


food_portion = deque(int(x) for x in input().split(', '))
stamina = deque(int(x) for x in input().split(', '))

peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
}
climbed_peaks = {}

while food_portion:

    adding_peaks()

conquered = [x for x in climbed_peaks.keys()]

if climbed_peaks:

    if len(climbed_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        print("Conquered peaks:")

    elif len(climbed_peaks) < 5:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        print("Conquered peaks:")
    print('\n'.join(conquered))

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")



