from utils.Arydraw.arydraw import draw_ary
import time
import random


def quicksort(ary, lo=0, hi=None):
    if hi is None:
        hi = len(ary) - 1
    if lo < hi:
        pivot = partition(ary, lo, hi)
        quicksort(ary, lo, pivot - 1)
        quicksort(ary, pivot + 1, hi)


def partition(ary, lo, hi):
    pivot_index = random.randint(lo, hi)
    ary[pivot_index], ary[hi] = (
        ary[hi],
        ary[pivot_index],
    )
    pivot = ary[hi]
    i = lo - 1
    for j in range(lo, hi):
        if ary[j] <= pivot:
            i += 1
            ary[i], ary[j] = ary[j], ary[i]
    ary[i + 1], ary[hi] = ary[hi], ary[i + 1]
    draw(ary)
    return i + 1


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=["yellow", "brightyellow"],
    )
    print(f"{'Quicksort' : >80}")
    time.sleep(0.03)
