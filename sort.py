from binary_search_tree import Tree
from math import log2


class Sort():
    @staticmethod
    def __swap(i: int, j: int, items: list):
        """Swaps elements of the specified list at the indices i and j.

        Args:
            i (int): Index to element to swap
            j (int): Index of element to swap
            items (list): List to swap elements
        """
        items[i], items[j] = items[j], items[i]

    @staticmethod
    def bubble_sort(items: list):
        """Performs bubble sort on the specified list. Modifies original list.
        <br>
        Continuously iterates through the list and swaps adjacent item pairs
        until the list is sorted.

        Comparision sort, in-place, stable

        Time complexity: 
        <li>Θ(n^2) worst/average case</li>
        <li>Θ(n) best case (already sorted)</li>

        Memory space: Θ(1)

        Args:
            items (list): The list to sort
        """
        # Keeps iterating until the list has no more items needed to swap
        swapped = True
        while swapped:
            swapped = False

            for j in range(0, len(items) - 1):
                if items[j] > items[j + 1]:
                    # Swaps adjacent items
                    Sort.__swap(j, j + 1, items)
                    swapped = True

    @staticmethod
    def selection_sort(items: list):
        """Performs selection sort on the specified list. Modifies original 
        list.<br>
        Continuously iterates through the list and swaps the end of a growing
        sorted sublist with the minimum item of the remaining list.

        Comparision sort, in-place, unstable

        Time complexity: Θ(n^2) all cases<br>
        Memory space: Θ(1)

        Args:
            items (list): The list to sort
        """
        for i in range(len(items) - 1):
            # Finds smallest index
            min_index = i
            for j in range(i + 1, len(items)):
                if items[j] < items[min_index]:
                    min_index = j

            # Swaps current index with minimum item
            Sort.__swap(i, min_index, items)

    @staticmethod
    def insertion_sort(items: list):
        """Performs insertion sort on the specified list. Modifies original 
        list.<br>
        Iterates through the list and inserts each item into a growing 
        sublist of sorted items.

        Comparision sort, in-place, stable

        Time complexity:
        <li>Θ(n^2) worst/average case</li>
        <li>Θ(n) best case (already sorted)</li>

        Memory space: Θ(1)

        Args:
            items (list): The list to sort
        """
        for i in range(1, len(items)):
            j = i
            while j > 0 and items[j] < items[j - 1]:
                Sort.__swap(j, j - 1, items)
                j -= 1

    @staticmethod
    def tree_sort(items: list):
        """Performs tree sort on a specified list. Modifies original list.<br>
        Iterates through the tree using in-order depth-first search and copies 
        the items in sorted order into the original list.

        Comparision sort, not in-place, stable

        Time complexity:
        <li>Θ(n^2) worst case (already sorted)</li>
        <li>Θ(nlg(n)) average/best case</li>

        Memory space: Θ(n)

        Args:
            items (list): The list to sort
        """
        tree = Tree(items)
        items[:] = tree.values()
        del tree

    @staticmethod
    def heapsort(items: list):
        """Peforms heapsort on a specified list. Modifies original list.<br>
        Transforms an unordered list into a max heap and continuously removes
        the top of the max heap to insert into the end of the list. Does not
        effectively use cashing.

        Comparision sort, in-place, unstable

        Time complexity: 
        <li>Θ(nlg(n)) worst/average case</li>
        <li>Θ(n) best case (all elements are identical)</li>
        
        Memory space: Θ(1)

        Args:
            items (list): The list to sort
        """

        # Converts list into max heap
        heap_end = len(items) - 1
        for i in range(heap_end // 2, -1, -1):
            Sort.__heapify(i, heap_end, items)

        # Continuously removes items from max heap
        while heap_end > 0:
            Sort.__swap(0, heap_end, items)
            Sort.__heapify(0, heap_end, items)
            heap_end -= 1

    @staticmethod
    def __heapify(index, heap_end, items: list):
        """Converts a sublist into a max heap.
        Assuming the left and right subtrees of a node at the index are max
        heaps, convert the tree starting from the node into a max heap.

        Time complexity: Θ(lgn)

        Args:
            index (integer): The index of the root of the tree
            heap_end (integer): The length of a list representing a heap
            items (list): The list representing a heap
        """
        current = index
        while current < heap_end:
            max_child = left = current * 2 + 1
            right = current * 2 + 2

            # Selects the larger of its two children, if any
            if right < heap_end and items[right] > items[left]:
                max_child = right

            # Checks if the parent is larger than the child
            if max_child < heap_end and items[max_child] > items[current]:
                Sort.__swap(current, max_child, items)

            current = max_child

    @staticmethod
    def quicksort(items: list):
        """Performs quicksort on the specified list. Modifies original list.<br>
        Partitions a list using the last element as a pivot key where 
        - elements to the left of the pivot are less than and equal to the pivot
        - elements to the right of the pivot

        Comparision sort, in-place, unstable

        Time complexity:
        <li>Θ(n^2) worst case</li>
        <li>Θ(nlg(n)) average/best case</li>

        Args:
            items (list): The list to sort
        """
        Sort.__quicksort(items, 0, len(items) - 1)
    
    @staticmethod
    def __quicksort(items: list, start: int, stop: int):
        """Performs quicksort on the specified list. Modifies original list.<br>
        Partitions a list using the last element as a pivot key where 
        - elements to the left of the pivot are less than and equal to the pivot
        - elements to the right of the pivot

        Comparision sort, in-place, unstable

        Time complexity:
        <li>Θ(n^2) worst case</li>
        <li>Θ(nlg(n)) average/best case</li>

        Args:
            items (list): The list to sort
        """
        if start >= stop:
            return

        pivot_index = Sort.__lomuto_partition(items, start, stop)

        Sort.__quicksort(items, start, pivot_index - 1)
        Sort.__quicksort(items, pivot_index + 1, stop)

    @staticmethod
    def __lomuto_partition(items: list, start: int, stop: int) -> int:
        """Splits a list into two halves.<br>
        Using the last element as a pivot, a list is bisected so that 
        - elements left of the pivot are smaller than or equal to it
        - elements right of the pivot are larger than it

        Time complexity: Θ(n)

        Args:
            items (list): The list to bisect
            start (int): The start index of the sublist of the list
            stop (int): The stop index of the sublist of the list

        Returns:
            int: The pivot index of quicksort
        """

        pivot_key = items[stop]
        pivot_index = start

        for inversion_index in range(start, stop):
            if items[inversion_index] <= pivot_key:
                Sort.__swap(pivot_index, inversion_index, items)
                pivot_index += 1

        Sort.__swap(pivot_index, stop, items)
        return pivot_index
    
    @staticmethod
    def __hoare_partition(items: list, start: int, stop: int) -> int:
         pass

    @staticmethod
    def merge_sort(items: list):
        """Performs merge sort on a specified list. Modifies original list.<br>
        Uses divide and conquer by continuously halfing the list into n sublists
        before merging them together in sorted order.  

        Comparision sort, not in-place, stable

        Time complexity: Θ(nlg(n)) all cases
        Memory space: Θ(n)

        Args:
            items (list): The list to sort
        """
        items[:] = Sort.__merge_sort(items)

    @staticmethod
    def __merge_sort(items: list) -> list:
        """Performs merge sort on a specified list and returns a new list. Does
        not modify the original list.<br>
        Uses divide and conquer by continuously halfing the list into n sublists
        before merging them together in sorted order.  

        Comparision sort, not in-place, stable

        Time complexity: Θ(nlg(n)) all cases
        Memory space: Θ(n)

        Args:
            items (list): The list to sort

        Returns:
            list: The left and right halfs of the list combined into a sorted
            list
        """
        if len(items) > 1:
            mid = len(items) // 2

            left = Sort.__merge_sort(items[:mid])
            right = Sort.__merge_sort(items[mid:])

            items = Sort.__merge(left, right)
            print(items)

        return items

    @staticmethod
    def __merge(left: list, right: list) -> list:
        """Merges two lists together in sorted order.

        Time complexity: Θ(n)
        Memory space: Θ(n)

        Args:
            left (list): One of the two lists to combine
            right (list): One of the two lists to combine

        Returns:
            list: A combined list of the two specified left and right lists in
            sorted order
        """
        left_index = 0

        while right:
            if left_index >= len(left) or right[0] < left[left_index]:
                left.insert(left_index, right.pop(0))

            left_index += 1

        del right
        return left

    @staticmethod
    def counting_sort(items: list):
        """Performs counting sort on a specified list. Modifies original list.
        <br>

        Linear sort, not in-place, stable

        Time complexity: Θ(n + k) all cases where k is the range of item values

        Args:
            items (list): The list to sort
        """
        pass

    @staticmethod
    def radix_sort(items: list):
        """Performs radix sort on a specified list of integers. Modifies
        original list.<br>
        Sorts digits by their least significant digit to their most 
        significant digit.

        Linear sort, in-place, stable

        Time complexity: Θ(n)

        Args:
            items (list): The list to sort
        """
        max_item = abs(max(items, key=abs))

        radix = 1
        while radix < max_item:
            pass
