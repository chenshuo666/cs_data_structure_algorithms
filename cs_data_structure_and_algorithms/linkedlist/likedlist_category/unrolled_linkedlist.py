from math import ceil #round up to an integer

class Node():
    def __init__(self):
        self.array = []
        self.next = None

    def __len__(self):
        return len(self.array)


class UnrolledLinkedList(object):
    """This class is used to implement an Unrolled Linked List"""
    def __init__(self, max_node_capacity=16):
        self.max_node_capacity = max_node_capacity
        self.length = 0
        self._head = None

    def is_empty(self):
        if self._head ==None:
            return True
        else:
            return False

    def get_length(self):
        """Get number of elements in Unrolled Linked List"""
        return self.length

    def check_index(self, index):
        """This function checks if the index is in range. """
        if 0 <= index < self.length:
            # index is positive
            return index
        elif 0 > index >= -self.length:
            # index is negative
            return self.length + index
        else:
            raise IndexError('Index is out of range')

    def balance(self, prev, cur):
        """Balances nodes after deleting an element"""

        while cur is not None:
            next_node = cur.next
            if next_node is None and len(cur) == 0:
                if self.length == 0:
                    self._head = None
                else:
                    prev.next = None
            elif next_node is not None and len(cur) < self.max_node_capacity/2:
                while len(cur) <= self.max_node_capacity/2:
                    cur.array.append(next_node.array.pop)
                    if len(next_node) == 0:
                        next_node = next_node.next
                        cur.next = next_node
                if len(next_node) >= self.max_node_capacity/2:
                     break
            cur = next_node

    def get_data_by_index(self, index):
        """Get item from array. Works with positive and negative values
        """
        index = self.check_index(index)
        node = self._head
        while node is not None:
            if index < len(node):
                return node.array[index]
            else:
                index -= len(node)
                node = node.next

    def get_data_by_self(self, obj):
        """Returns True if element is found in list, otherwise it returns false"""
        if self._head is None:
            return False
        else:
            contains_object = False
            node = self._head
            while node is not None:
                if obj in node.array:
                    contains_object = True
                node = node.next
            return contains_object

    def travel_print(self):
        """Prints string representation of Unrolled Linked List"""
        node = self._head
        string = '{'
        while node is not None:
            node_array = node.array
            string += '['
            for index, element in enumerate(node_array):
                string += str(element) + '' if index == len(node_array) - 1 else str(element) + ', '
            string += ']'
            node = node.next
            string += '' if node is None else ', '
        string += '}'
        return string

    def update(self, key, value):
        """Set item at index to a certain value
        """
        index = self.check_index(key)
        node = self._head
        while node is not None:
            if index < len(node):
                node.array[index] = value
                break
            else:
                index -= len(node)
                node = node.next

    def insert_append(self, data):
        """Adds data to end of Unrolled Linked List"""
        if self._head is None:
            node = Node()
            node.array.append(data)
            node.next = None
            self._head = node
        else:
            node = self._head
            while node.next is not None:
                node = node.next
            if len(node) < self.max_node_capacity:
                node.array.append(data)
            else:
                new_node = Node()
                new_node.array = node.array[int(ceil(len(node)/2)):]
                new_node.array.append(data)
                node.array = node.array[:int(ceil(len(node)/2))]
                node.next = new_node

        self.length += 1


    def delete_by_index(self, index):
        """Delete item from list"""
        index = self.check_index(index)
        prev = None
        node = self._head
        while node is not None:
            if index < len(node):
                del node.array[index]
                self.length -= 1
                self.balance(prev,node)
                break
            else:
                index -= len(node)
                prev = node
                node = node.next

    def __iter__(self):
        """Returns iterator for Unrolled Linked List"""
        node = self._head
        iter_array = []
        while node is not None:
            iter_array += node.array
            node = node.next
        for element in iter_array:
            yield element

    def __reversed__(self):
        """Returns reverse iterator for Unrolled Linked List"""
        node = self._head
        iter_array = []
        while node is not None:
            iter_array += node.array
            node = node.next
        for element in reversed(iter_array):
            yield element
