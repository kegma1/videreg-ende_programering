import time
from test_list import lst

def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1)
        quickSortHelper(lst, pivotIndex + 1, last)

# Partition lst[first..last] 
def partition(lst, first, last):
    pivot = lst[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and lst[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and lst[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            lst[high], lst[low] = lst[low], lst[high]

    while high > first and lst[high] >= pivot:
        high -= 1

    # Swap pivot with lst[high]
    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


# A test function 
def main():
    st = time.process_time()
    quickSort(lst)
    et = time.process_time()
    res = et - st
    print(res)
    print(is_sorted(lst))

main()