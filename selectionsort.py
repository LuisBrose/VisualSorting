from utils.Arydraw.arydraw import draw_ary
import time


def selectionsort(ary):
    a_length = len(ary)
    for i in range(a_length):
        smallest = i
        for j in range(i + 1, a_length):
            if ary[j] < ary[smallest]:
                smallest = j
        if smallest != i:
            ary[i], ary[smallest] = ary[smallest], ary[i]
            draw(ary)


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=["blue", "brightblue", "magenta", "cyan"],
    )
    print(f"{'Selectionsort' : >110}")
    time.sleep(0.01)
