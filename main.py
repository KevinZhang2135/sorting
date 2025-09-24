from binary_search_tree import Tree
from point import Point
from sort import Sort

from random import randint
from time import perf_counter

def is_sorted(list):
    for i in range(1, len(list)):
        if list[i - 1] > list[i]:
            return False
        
    return True

def testSorting(sorting_method, n):
    success = False
    for _ in range(1000):
        items = [randint(1, 999) for _ in range(n)]
        sorting_method(items)

        if not (success := is_sorted(items)):
            break
    
    success = 'success' if success else 'fail'
    print(f'"{sorting_method.__name__}" sort on list of size {n}: {success}')

def timeSorting(sorting_method, items):
    start_time = perf_counter()
    sorting_method(items)
    total_time = perf_counter() - start_time

    print(f'{f"{sorting_method.__name__}":>16}: {total_time:>6.4f} s')

if __name__ == '__main__':
    items = [randint(1, 999) for _ in range(10_000)]

    testSorting(Sort.heapsort, 10_000)
    