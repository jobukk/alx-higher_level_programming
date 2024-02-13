#!/usr/bin/python3
class Node:
    def __init__(self,data,next=None):
        self.__data = data
        self.__next_node = next
    @property    
    def data(self):
        return self.__data
    @property
    def set_data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
        
    def next_node(self):
        return self.__next_node
    
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
class SinglyLinkedList:
    def __init__(self,head=None):
        self.__head = head
        
    def __str__(self):
        current = self.__head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
    def append(self, data):
        if not self.__head:
            self.__head = Node(data)
            return
        current = self.__head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)
        
    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
