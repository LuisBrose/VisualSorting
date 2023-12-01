from utils.Arydraw.arydraw import draw_ary
import time


def bubblesort(ary):
    n = len(ary)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if ary[i] > ary[i + 1]:
                ary[i], ary[i + 1] = ary[i + 1], ary[i]
                swapped = True
        draw(ary)


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=["red", "brightred", "magenta"],
    )
    print(f"{'Bubblesort' : >110}")
    time.sleep(0.01)
