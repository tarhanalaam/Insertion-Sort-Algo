# Insertion-Sort-Algo

> Cause merge sort takes up too much memory.

A small, dependency-free Python implementation of insertion sort, with a simple timing harness to see how it performs on a few sample arrays.

## How it works

Insertion sort builds the sorted array one element at a time. For each element, it walks backward through the already-sorted portion of the array, shifting larger elements to the right until it finds the correct spot to insert the current element.

```python
def insertion_sort(arr: list[object]) -> list[object]:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr
```

- **Time complexity:** O(n²) worst/average case, O(n) best case (already sorted)
- **Space complexity:** O(1) — sorts in place
- **Stable:** yes (equal elements keep their relative order)

## Project structure

```
.
├── main.py           # Sorting algorithm + timing/test runner
├── test_cases.py      # Sample input arrays
├── pyproject.toml     # Project metadata
├── .python-version     # Pinned Python version
└── .gitignore
```

## Requirements

- Python (see `.python-version` for the pinned version)
- No external dependencies

## Usage

Clone the repo and run `main.py` directly:

```bash
git clone https://github.com/tarhanalaam/Insertion-Sort-Algo.git
cd Insertion-Sort-Algo
python main.py
```

This will sort each sample array from `test_cases.py`, print the result, and report how long each run took:

```
[1, 1, 2, 3, 4, 5, 6, 9]
First run took: 0.00001 seconds
[1, 2, 3, 4, 5]
Second run took: 0.00001 seconds
[]
Third run took: 0.00000 seconds
```

## Test cases

`test_cases.py` defines three sample arrays:

| Name | Value | What it covers |
|---|---|---|
| `first_case` | `[3, 1, 4, 1, 5, 9, 2, 6]` | Random unsorted input with a duplicate |
| `second_case` | `[5, 4, 3, 2, 1]` | Reverse-sorted (worst case for insertion sort) |
| `third_case` | `[]` | Empty input |

## Notes / caveats

- Timing is measured with `time.time()`, which has limited resolution — for arrays this small, the numbers mostly reflect interpreter overhead rather than the algorithm itself. For meaningful benchmarks, try much larger arrays (1,000+ elements) or `time.perf_counter()`.
- The script currently prints results rather than asserting them against expected output, so correctness is verified by inspection rather than automated checks.

## License

No license specified yet.