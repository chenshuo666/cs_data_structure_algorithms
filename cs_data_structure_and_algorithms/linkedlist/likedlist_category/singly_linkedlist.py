#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

"""Initialize the node, the node includes the currently stored content and a pointer to the next node"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList(object):
    def __init__(self):
        """
        Initialize SinglyLinkedList 
        """
        self.length = 0
        self.head = None
        self.record = []

    def is_empty(self):
        """
        Determine if the list is empty
        """
        if self.head == None:
            return True
        else:
            return False

    def get_length(self):
        """
        Get the length of the linked list
        """
        cur = self.head
        if cur:
            i = 1
            while cur.next:
                cur = cur.next
                i += 1
            return i
        else:
            return 0

    def get_data_by_index(self, index):
        '''Determine whether data exists by index'''
        j = 0
        p = self.head
        if self.is_empty():
            return -1
        else:
            while p.next != 0 and j < index:
                p = p.next
                j += 1
            if j == index:
                return p.data
            else:
                return -1

    def get_data_by_self(self, data):
        '''Determine whether data exists by data'''
        cur = self.head
        j = 0
        if self.is_empty():
            print('Linklist is empty.')
            return
        else:
            while cur != None:
                if cur.data == data:
                    print("the index of the %s is %s".format(data, j))
                    return True
                cur = cur.next
                j += 1
            return False

    def travel_print(self):
        """ traverses the entire list and outputs the value of the linked list """
        if self.is_empty():
            print("Linked list's length is 0")
        else:
            node = self.head
            print("head -->", node.data, end=' ')
            while node.next:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def insert_head(self, data):
        """Insert data at the head of the list"""
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_append(self, this_node):
        '''Insert data at the end of the list'''
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            # When the linked list is empty, point the head pointer to the current node
            self.head = this_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = this_node
        self.length += 1

    def insert(self, value, index):
        """
        List insert operation
        :param value: The value to be inserted
        :param index: The position to be inserted
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # The index value is out of range and prompts and exits
                print("Index value is out of range.")
                return
            else:
                # Get the current node object and head
                this_node = Node(data=value)
                cur = self.head

                if index == 0:
                    # The index value is 0, insert the head of the linked list
                    self.head = this_node
                    this_node.next = cur
                    return

                while index - 1:
                    cur = cur.next
                    index -= 1
                # Disassemble the current node from the next node, this_node points to the next node,
                # and the previous node points to this_node
                this_node.next = cur.next
                cur.next = this_node
                self.length += 1
                return

        else:
            print("Index value is not int.")
            return


    def delete_node(self, index):
        """
        Delete a node in a location in the linked list
        :param index: Location index
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # The index value is out of range and prompts and exits
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    self.head = self.head.next
                else:
                    cur = self.head
                    while index - 1:
                        cur = cur.next
                        index -= 1
                    cur.next = cur.next.next
                    self.length -= 1
                    return
        else:
            print("Index value is not int.")
            return

    def update(self, value, index):
        """modifies the value for a node in a location in the list"""

        if type(index) is int:
            if index > self.length:
                # The index value is out of range and prompts and exits
                print("Index  is out of range.")
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    this_node.next = self.head.next
                    self.head = this_node
                else:
                    cur = self.head
                    while index - 1:
                        cur = cur.next
                        index -= 1
                    this_node.next = cur.next.next
                    cur.next = this_node
                    return
        else:
            print("Index value is not int.")
            return

    def get_value(self, index):
        """
        Get the value of a node in the linked list
        :param index: location index
        :return: the node value, int or not
        """
        if type(index) is int:
            if index > self.length:
                # The index value is out of range and prompts and exits
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    return self.head.data
                else:
                    cur = self.head
                    while index - 1:
                        cur = cur.next
                        index -= 1
                    return cur.next.data
        else:
            print("Index value is not int.")
            return

    def clear_singly_linkedlist(self):
        """Empty list"""
        self.head = None
        self.length = 0
        print("Clear the linked list finished.")

    def reverse(self, root):
        if root == None:
            return -1
        elif root.next == None:
            return -1
        else:
            cur = root.next
            root.next = cur.next
            cur.next = root
            root = cur
            root.next.next = self.reverse(root.next.next)
            return root

    def merge(self, a, b):

        global result
        if a.data <= b.data:
            result = a
            self.record.append(a.data)
            result.next = self.merge(a.next,b)
        else:
            result = b
            self.record.append(b.data)
            result.next = self.merge(b.next, a)
        return result


if __name__ == '__main__':
    t1 = SinglyLinkedList()
    for i in range(10):
        t1.insert_append(i)
    print(t1.head.next.data)
    t1.insert_head(99)
    t1.insert_head(34)
    t1.travel_print()

    a = [1, 3, 6, 7, 13, 15, 17, 23, 45, 567, 6865, 46758]
    t2 = SinglyLinkedList()
    for i in range(len(a)):
        t2.insert_append(a[i])
    m=t1.head
    n=t2.head
    t1.merge(m,n)
    print(t1.record)
