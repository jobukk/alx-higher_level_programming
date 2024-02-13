#!/usr/bin/python3

"""Define singly-linked list."""


class Node:
    """Node of a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize new node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new node.
        """    
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get/Set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property    
    def next_node(self):
        """Get/Set the next_node of the Node."""
        return (self.__next_node)
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self,head=None):
        """Initialize a new SinglyLinkedList."""
        self.__head = head
        
    def __str__(self):
        """Define the print() representation of SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
    def append(self, data):
        if not self.__head:
            self.__head = Node(data)
            return
        current = self.__head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)
        
    def sorted_insert(self, value):
          """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
