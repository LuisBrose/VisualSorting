from utils.Arydraw.arydraw import draw_ary
import time
import random


def bogosort(ary):
    while not is_sorted(ary):
        a = random.randint(0, len(ary) - 1)
        b = random.randint(0, len(ary) - 1)
        ary[a], ary[b] = ary[b], ary[a]
        draw(ary)


def is_sorted(ary):
    for i in range(len(ary) - 1):
        if ary[i] > ary[i + 1]:
            return False
    return True


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=[
            "magenta",
            "green",
            "red",
            "blue",
            "yellow",
        ],
    )
    print(f"{'Bogosort': >80}")
    time.sleep(0.03)
