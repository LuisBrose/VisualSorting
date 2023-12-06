from utils.Arydraw.arydraw import draw_ary, os_clear
import time


class MergesortState:
    original_list_length = 0
    iterations = []

    def __init__(self, original_list_length) -> None:
        self.original_list_length = original_list_length

    def has_iteration(self, depth):
        return len(self.iterations) - 1 >= depth

    def iteration_completed(self, depth):
        return (
            len(self.iterations[self.get_index(depth)])
            == self.original_list_length
        )

    def draw_iteration_replay(self, depth):
        if depth == 0:
            for iteration in self.iterations:
                draw(iteration)

    def get_index(self, depth):
        return len(self.iterations) - 1 - depth

    def update_state_at_recursion_depth(self, partial_array, depth):
        if self.has_iteration(depth):
            self.iterations[self.get_index(depth)] += partial_array
        else:
            self.iterations.append([])
            self.update_state_at_recursion_depth(partial_array, depth)


def mergesort(ary, state=None, depth=0):
    if not state:
        state = MergesortState(len(ary))
    if len(ary) <= 1:
        return ary
    left_ary = mergesort(ary[: len(ary) // 2], state, depth + 1)
    right_ary = mergesort(ary[len(ary) // 2 :], state, depth + 1)
    result = merge(left_ary, right_ary)
    state.update_state_at_recursion_depth(result, depth)
    state.draw_iteration_replay(depth)
    return result


def merge(left, right):
    left = list(left)
    right = list(right)
    result = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left):
        result.append(left.pop(0))
    while len(right):
        result.append(right.pop(0))
    return result


def draw(ary):
    draw_ary(
        ary=ary,
        height=24,
        color_sequence=[
            "red",
            "brightred",
        ],
    )
    print(f"{'Mergesort' : >80}")
    time.sleep(0.5)
