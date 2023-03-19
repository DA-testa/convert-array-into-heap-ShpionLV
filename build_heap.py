from typing import List, Tuple


def swap(data: List[int], i: int, j: int) -> None:
    data[i], data[j] = data[j], data[i]


def heapify(parent_index: int, data: List[int], swaps: List[Tuple[int, int]]) -> None:
    left_child_index = parent_index * 2 + 1
    right_child_index = parent_index * 2 + 2
    smallest_child_index = parent_index

    if left_child_index < len(data) and data[left_child_index] < data[smallest_child_index]:
        smallest_child_index = left_child_index

    if right_child_index < len(data) and data[right_child_index] < data[smallest_child_index]:
        smallest_child_index = right_child_index

    if smallest_child_index != parent_index:
        swap(data, smallest_child_index, parent_index)
        swaps.append((parent_index, smallest_child_index))
        heapify(smallest_child_index, data, swaps)


def build_heap(data: List[int]) -> List[Tuple[int, int]]:
    swaps = []
    last_non_leaf_index = (len(data) - 2) // 2

    for i in range(last_non_leaf_index, -1, -1):
        heapify(i, data, swaps)

    return swaps


def main() -> None:
    test_type = input("Choose a test type (I or F): ").lower()

    if test_type == "i":
        n = int(input("Node amount: "))
        data = list(map(int, input("Nodes: ").split()))
    elif test_type == "f":
        filename = input("Enter file name: ")
        with open(f"tests/{filename}", 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        raise ValueError("Invalid input type. Expected I or F.")

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
