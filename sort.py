from binary_search_tree import Tree


class Sort():
    @staticmethod
    def __swap(i: int, j: int, items: list):
        """Swaps elements of the specified list at the indices i and j

        Args:
            i (int): Index to element to swap
            j (int): Index of element to swap
            items (list): List to swap elements
        """
        items[i], items[j] = items[j], items[i]

    @staticmethod
    def bubble_sort(items: list):
        """Performs bubble sort on the specified list.<br>
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
        """Performs selection sort on the specified list.<br>
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
        """Performs insertion sort on the specified list.<br>
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
        """Performs tree sort on a specified list.<br>
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
        """Peforms heapsort on a specified list.<br>
        Transforms an unordered list into a max heap and continuously removes
        the top of the max heap to insert into the end of the list. Does not
        effectively use cashing.

        Comparision sort, in-place, unstable

        Time complexity: Θ(nlg(n)) all cases
        Memory space: Θ(1)

        Args:
            items (list): The list to sort
        """
        # Adds each item into heap
        for i in range(1, len(items)):
            parent_index = (i - 1) // 2

            # Keeps bubbling up if greater
            while parent_index >= 0 and items[i] > items[parent_index]:
                Sort.__swap(i, parent_index, items)

                i = (i - 1) // 2
                parent_index = (i - 1) // 2

        # Continuously removes items from max heap
        heap_end = len(items) - 1
        while heap_end > 0:
            Sort.__swap(0, heap_end, items)

            current = 0
            while current < heap_end:
                next = left = current * 2 + 1
                right = current * 2 + 2

                # Selects the larger of its two children, if any
                if right < heap_end:
                    if left >= heap_end or items[right] > items[left]:
                        next = right

                if next < heap_end and items[next] > items[current]:
                    Sort.__swap(current, next, items)

                current = next

            heap_end -= 1

    @staticmethod
    def quicksort(items: list):
        """Performs quicksort on the specified list.<br>

        Comparision sort, in-place, unstable

        Time complexity:
        <li>Θ(n^2) worst case</li>
        <li>Θ(nlg(n)) average/best case</li>

        Args:
            items (list): The list to sort
        """
        pivot = items[-1]

    @staticmethod
    def __quicksort(items: list, start: int, stop: int) -> int:
        """Performs quicksort on 

        Args:
            items (list): _description_
            start (int): _description_
            stop (int): _description_

        Returns:
            int: The pivot index of quicksort
        """
        left, right = start, stop
        while left <= right:
            pass

    @staticmethod
    def merge_sort(items: list):
        """Performs merge sort on a specified list.<br>
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
        """Performs merge sort on a specified list.<br>
        Uses divide and conquer by continuously halfing the list into n sublists
        before merging them together in sorted order.  

        Comparision sort, not in-place, stable

        Time complexity: Θ(nlg(n)) all cases

        Args:
            items (list): The list to sort

        Returns:
            list: The left and right halfs of the list combined into a sorted
            list
        """
        sorted = items
        if len(items) > 1:
            mid = len(items) // 2

            left = Sort.__merge_sort(items[:mid])
            right = Sort.__merge_sort(items[mid:])

            sorted = Sort.__merge(left, right)

        return sorted

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
        """Performs counting sort on a specified list.<br>

        Linear sort, not in-place, stable

        Time complexity: Θ(n + k) all cases where k is the range of item values

        Args:
            items (list): The list to sort
        """
        pass

    @staticmethod
    def radix_sort(items: list):
        """Performs radix sort on a specified list of integers.<br>
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
