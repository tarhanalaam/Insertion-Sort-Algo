# My Modules
import time
from test_cases import *

# Main Algo
def insertion_sort(arr: list[object]) -> list[object]:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

# Test & Run
if __name__ == "__main__":
    try:
        first_time = time.time()
        print(insertion_sort(first_case))
        second_time = time.time()
        print(f"First run took: {round(second_time - first_time, 5)} seconds")
        first_time = time.time()
        print(insertion_sort(second_case))
        second_time = time.time()
        print(f"Second run took: {round(second_time - first_time, 5)} seconds")
        first_time = time.time()
        print(insertion_sort(third_case))
        second_time = time.time()
        print(f"Third run took: {round(second_time - first_time, 5)} seconds")
    except Exception as e:
        print(f"Oops something unexpected: {e} happened!")