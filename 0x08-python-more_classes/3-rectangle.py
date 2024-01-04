#!/usr/bin/python3
"""Module that defines Node and SinglyLinkedList classes."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the node.

        Args:
            data: Data to be stored in the node.
            next_node: Reference to the next node in the linked list.

        Raises:
            TypeError: If data is not an integer or if next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value: Data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value: Next node in the linked list.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize the singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value: Data to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
