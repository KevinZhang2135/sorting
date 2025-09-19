from collections.abc import Iterable
from typing import Any

class Tree:
    class __Node:
        def __init__(self, value: Any):
            """Initializes a new node with the specified value.

            Args:
                value (Any): The value of the new node
            """
            self.value = value
            self.left, self.right, = None, None

        def min(self) -> Any:
            """Returns the minimum item in the subtree.

            Returns:
                Any: The minimum item in the subtree
            """
            min_item = self.value
            if self.left:
                min_item = self.left.min()

            return min_item

        def max(self) -> Any:
            """Returns the maximum item in the subtree.

            Returns:
                Any: The maximum item in the subtree
            """
            max_item = self.value
            if self.right:
                max_item = self.right.max()

            return max_item

        def add(self, value: Any):
            """Inserts node into the subtree.

            Args:
                value (Any): The value of the node to be inserted
            """
            # Value is inserted on the left branch
            if value <= self.value:
                if self.left:
                    self.left.add(value)

                else:
                    self.left = self.__class__(value)

            # Value is inserted on the right branch
            else:
                if self.right:
                    self.right.add(value)

                else:
                    self.right = self.__class__(value)

        def values(self) -> list:
            """Returns a list of of all the items in the subtree in sorted 
            order.

            Returns:
                list: List of all the items in the subtree in sorted order
            """
            left = self.left.values() if self.left else []
            right = self.right.values() if self.right else []

            return [*left, self.value, *right]

        def __contains__(self, value: Any):
            """Determines whether a value is in the subtree.

            Time complexity O(log(n))

            Args:
                value (Any): The value to be searched for

            Returns:
                bool: Whether the value is in the subtree
            """
            found = self.value == value

            if not found:
                if value <= self.value:
                    if self.left:
                        found = self.left.__contains__(value)

                elif self.right:
                    found = self.right.__contains__(value)

            return found

        def __str__(self) -> str:
            """Returns a string containing all the items of the subtree in
            sorted order, delimited by a space.

            Returns:
                str: All the items in the subtree in sorted order, delimited
                by a space
            """
            left = self.left if self.left else ''
            right = self.right if self.right else ''

            return f'{left}{self.value} {right}'

    def __init__(self, items: list = None):
        """Creates an empty tree.

        Args:
            items (list, optional): The list of items to populate the tree with.
            Defaults to None.
        """
        self.__root = None
        self.__length = 0

        if items:
            for item in items:
                self.add(item)

    def min(self) -> Any:
        """Returns the minimum item in the subtree.

        Returns:
            Any: The minimum item in the tree; None if there are not any
            items in the tree
        """
        min_item = None
        if self.__root:
            min_item = self.__root.min()

        return min_item

    def max(self) -> Any:
        """Returns the maximum item in the subtree.

        Returns:
            Any: The maximum item in the tree: None if there are not any
            items in the tree
        """
        max_item = None
        if self.__root:
            max_item = self.__root.max()

        return max_item

    def add(self, value: Any):
        """Inserts node into tree.

        Args:
            node (Any): The value of the node to be inserted
        """
        self.__length += 1
        if self.__root:
            self.__root.add(value)

        else:
            self.__root = self.__Node(value)

    def pop(self, value: Any):
        """Removes an item from the tree.

        Args:
            value (Any): The value of the node to be removed
        """
        if self.__root:
            self.__root = self.__pop(self.__root, value)

    def __pop(self, node: __Node, value: Any) -> __Node:
        """Removes an item from the subtree.

        Args:
            node (_Node): The specified node
            value (Any): The value of the node to be removed

        Returns:
            _Node:  The reference of the node to the parent node
        """
        if value < node.value:
            if node.left:
                node.left = self.__pop(node.left, value)

        elif value > node.value:
            if node.right:
                node.right = self.__pop(node.right, value)

        else:
            if node.left:
                left_max = node.left.max()
                node.value = left_max
                node.left = self.__pop(node.left, left_max)

            elif node.right:
                right_min = node.right.min()
                node.value = right_min
                node.right = self.__pop(node.right, right_min)

            else:
                node = None
                self.__length -= 1

        return node

    def __len__(self) -> int:
        """Returns the number of items in the tree.

        Returns:
            int: The number of items in the tree
        """
        return self.__length

    def values(self) -> list:
        """Returns a list of of all the items in the tree in sorted order.

        Returns:
            list: List of all the items in the tree in sorted order
        """
        return self.__root.values()

    def __iter__(self) -> Iterable:
        """Returns an iterator of all items in order.

        Returns:
            Iterable: The iterator of all items in order
        """
        return iter(self.__root.values())

    def __reversed__(self) -> Iterable:
        """Returns an iterator of all items in reverse order.

        Returns:
            Iterable: The iterator of all items in reverse order
        """
        return iter(reversed(self.__root.values()))

    def __contains__(self, value: Any) -> bool:
        """Determines whether a value is in the tree.

        Time complexity O(log(n))

        Args:
            value (Any): The value to be searched for

        Returns:
            bool: Whether the value is in the tree
        """
        return self.__root and self.__root.__contains__(value)

    def __str__(self) -> str:
        """Returns a string containing all the items of the tree in sorted
        order, delimited by a space.

        Returns:
            str: All the items in the tree in sorted order, delimited by a 
            space
        """
        return self.__root.__str__().strip()
