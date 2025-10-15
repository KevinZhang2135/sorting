from binary_search_tree import Tree
from point import Point
from sort import Sort
from justin import justinheapsort

from random import randint
from time import perf_counter
from math import log2, ceil

def is_sorted(items):
    """Determines whether the list is in sorted order

    Args:
        list (list): The list to check if it is in sorted order

    Returns:
        bool: Whether if the list is sorted
    """
    for i in range(1, len(items)):
        if items[i - 1] > items[i]:
            return False
        
    return True

def testSorting(sorting_method, n):
    """Runs 1000 tests of a sorting algorithm for lists of size n and prints 
    whether all runs were successful

    Args:
        sorting_method (function): The sorting algorithm to test
        n (int): The size of the randomized list in each test
    """
    success = False
    for _ in range(1000):
        items = [randint(1, 999) for _ in range(n)]
        sorting_method(items)

        if not (success := is_sorted(items)):
            break
    
    success = 'success' if success else 'fail'
    print(f'"{sorting_method.__name__}" sort on list of size {n}: {success}')

def timeSorting(sorting_method, items):
    """Prints the time a sorting algorithm took to sort a list. Does not create
    a copy of the list

    Args:
        sorting_method (function): The sorting algorithm to test
        items (list): The list used to time a sort
    """
    start_time = perf_counter()
    sorting_method(items)
    total_time = perf_counter() - start_time

    print(f'{f"{sorting_method.__name__}":>16}: {total_time:>6.4f} s')

def binary_search(items, element):
    index = -1
    start = 0
    end = len(items) - 1

    while start <= end:
        mid = (start + end) // 2
        
        if element < items[mid]:
            end = mid - 1

        elif element > items[mid]:
            start = mid + 1

        else:
            index = mid
            break

    return index


if __name__ == '__main__':
    pass