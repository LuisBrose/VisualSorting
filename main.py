import numpy as np
from insertionsort import insertionsort
from selectionsort import selectionsort
from bubblesort import bubblesort
from quicksort import quicksort
from heapsort import heapsort


def main():
    rng = np.random.default_rng()
    ary = rng.integers(low=-100, high=101, size=200)
    ary2 = rng.integers(low=-100, high=101, size=200)
    ary3 = rng.integers(low=-100, high=101, size=200)
    ary4 = rng.integers(low=-100, high=101, size=200)
    ary5 = rng.integers(low=-100, high=101, size=200)
    selectionsort(ary)
    insertionsort(ary2)
    bubblesort(ary3)
    quicksort(ary4)
    heapsort(ary5)


if __name__ == "__main__":
    main()
