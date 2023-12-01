from utils.Arydraw.arydraw import draw_ary
import time


def heapsort(ary):
    count = len(ary)
    start = count // 2
    end = count
    while end > 1:
        if start > 0:
            start -= 1
        else:
            end -= 1
            ary[end], ary[0] = ary[0], ary[end]
        root = start
        while root * 2 + 1 < end:
            child = root * 2 + 1
            if child + 1 < end and ary[child] < ary[child + 1]:
                child += 1
            if ary[root] < ary[child]:
                ary[root], ary[child] = ary[child], ary[root]
                root = child
            else:
                break
        draw(ary)


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=[
            "brightwhite",
            "magenta",
            "brightblack",
            "red",
        ],
    )
    print(f"{'Heapsort' : >110}")
    time.sleep(0.01)
