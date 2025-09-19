from binary_search_tree import Tree
from point import Point
from sort import Sort
from random import randint

def is_sorted(list):
    for i in range(1, len(list)):
        if list[i - 1] > list[i]:
            return False
        
    return True

def testSorting(method):
    success = False
    for i in range(2000):
        elements = [randint(1, 99) for i in range(100)]
        method(elements)

        if not (success := is_sorted(elements)):
            break

    print(success)

# testSorting(Sort.merge_sort)
test_list = [Point(10, 1), Point(10, 2), Point(5, 1)]
Sort.selection_sort(test_list)

for point in test_list:
    print(point)
