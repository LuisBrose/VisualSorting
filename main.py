import numpy as np
from insertionsort import insertionsort
from selectionsort import selectionsort
from bubblesort import bubblesort
from quicksort import quicksort
from heapsort import heapsort
from bitonicsort import bitonicsort


def main():
    rng = np.random.default_rng()
    selectionsort(rng.integers(low=-100, high=101, size=200))
    insertionsort(rng.integers(low=-100, high=101, size=200))
    bubblesort(rng.integers(low=-100, high=101, size=200))
    quicksort(rng.integers(low=-100, high=101, size=200))
    heapsort(rng.integers(low=-100, high=101, size=200))
    bitonicsort(rng.integers(low=-100, high=101, size=128))


if __name__ == "__main__":
    main()
