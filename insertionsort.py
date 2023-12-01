from utils.Arydraw.arydraw import draw_ary
import time


def insertionsort(ary):
    for i in range(1, len(ary)):
        value = ary[i]
        j = i
        while j > 0 and ary[j - 1] > value:
            ary[j] = ary[j - 1]
            j = j - 1
        ary[j] = value
        draw(ary)


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=["green", "brightgreen"],
    )
    print(f"{'Insertionsort' : >110}")
    time.sleep(0.01)
