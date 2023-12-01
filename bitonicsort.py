from utils.Arydraw.arydraw import draw_ary
import time


def bitonicsort(ary):
    n = len(ary)
    k = 2
    while k < n:
        j = k // 2
        while j > 0:
            for i in range(n):
                l = i ^ j
                if l > i and (
                    (i & k == 0 and ary[i] > ary[l])
                    or (i & k != 0 and ary[i] < ary[l])
                ):
                    ary[i], ary[l] = ary[l], ary[i]
                    draw(ary)
            j //= 2
        k *= 2


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=[
            "brightcyan",
            "cyan",
        ],
    )
    print(f"{'Bitonicsort': >80}")
    time.sleep(0.03)
