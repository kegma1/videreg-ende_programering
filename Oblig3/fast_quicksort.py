import time
from test_list import lst

def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex - 1)
        quickSortHelper(lst, pivotIndex + 1, last)


def choose_pivot(lst, first, last):
    middle = (first + last) // 2

    first_elm = lst[first]
    middle_elm = lst[middle]
    last_elm = lst[last]

    if (first_elm <= middle_elm <= last_elm) or (last_elm <= middle_elm <= first_elm):
        return middle
    if (middle_elm <= first_elm <= last_elm) or (last_elm <= first_elm <= middle_elm):
        return first
    else:
        return last


# Partition lst[first..last] 
def partition(lst, first, last):
    pivot_index = choose_pivot(lst, first, last)
    lst[first], lst[pivot_index] = lst[pivot_index], lst[first]

    pivot = lst[first]
    low = first + 1
    high = last


    while high > low:
        while low <= high and lst[low] <= pivot:
            low += 1

        while low <= high and lst[high] > pivot:
            high -= 1

        if high > low:
            lst[high], lst[low] = lst[low], lst[high]

    while high > pivot_index and lst[high] >= pivot:
        high -= 1

    lst[first], lst[high] = lst[high], lst[first]

    return high

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