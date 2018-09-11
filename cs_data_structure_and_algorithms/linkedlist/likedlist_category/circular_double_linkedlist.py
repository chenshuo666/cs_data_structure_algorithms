#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

"""Initialize the node, the node includes the currently stored content and a pointer to the next node"""

class Node(object):
    """circular double linked list node"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)

class CircularDoubleLinkList(object):
    """circular double linked list"""

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        """Determine if the list is empty"""
        if self.head == None:
            return True
        else:
            return False

    def get_length(self):
        """Get the length of the linked list"""
        current_node = self.head
        if current_node:
            i = 1
            while current_node.next != self.head:
                current_node = current_node.next
                i += 1
            return i
        else:
            return 0

    def get_data_by_index(self, index):
        '''Determine whether data exists by index'''
        j = 0
        cur = self.head
        if self.is_empty():
            print('Linklist is empty.')
            return
        else:

            while cur.next != 0 and j < index:
                cur = cur.next
                j += 1
            if j == index:
                return cur.data
            else:
                print('Target is not exist!')

    def get_data_by_self(self, data):
        '''Determine whether data exists by data'''
        cur = self.head
        j = 0
        if self.is_empty():
            print('Linklist is empty.')
            return
        else:
            while cur.next!= self.head:
                if cur.data == data:
                    print("the index of the %d is %d" % (data, j))
                    return True
                cur = cur.next
                j += 1
            return False

    def travel_print(self):
        """Traversing the linked list"""

        if self.is_empty():
            print("Linked list's length is 0")
        else:
            node = self.head
            print("head -->", node.data, end=' ')
            while node.next !=self.head:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def insert_head(self, data):
        """Insert data at the head of the list"""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = node
            node.prev = node

        else:
            node.next = self.head  # The node's next is set to the current head
            node.prev = self.head.prev  # The prev of node is set to the front of the head prev
            self.head.prev.next = node  # Now the next element of the head is set to node next.
            self.head.prev = node  # Now the front of the head is changed to node
            self.head = node  # Change the head pointer

    def insert_append(self, data):
        """Insert data at the end of the list"""
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
            node.prev = self.head
        else:
            node.next = self.head  # The next node of node is set to the head node
            node.prev = self.head.prev  # The front of the node is set to the front of the head
            self.head.prev.next = node  # The successor of the head precursor is set to node
            self.head.prev = node  # Change the head of the head to node

    def insert(self, pos, data):
        """
        List insert operation
        :param value: The value to be inserted
        :param index: The position to be inserted
        :return: None
        """
        if pos <= 0:
            self.insert_head(data)
        elif pos > (self.get_length() - 1):
            self.insert_append(data)
        else:
            node = Node(data)
            cur = self.head
            count = 0
            # Move to the previous position in the specified position
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def delete_by_data(self, data):
        """delete element by data"""
        if self.is_empty():
            return
        else:
            try:
                cur = self.head
                if cur.data == data:
                    # If the element of the first node is the element to be deleted, there is only one element
                    if cur.next == None:
                        self.head = None

                    else:
                        # If the linked list has more than one node
                        # First find the tail node, point the next node's next to the second node
                        while cur.next != self.head:
                            cur = cur.next
                        # cur pointed to the tail node
                        cur.next = self.head.next
                        self.head = self.head.next
                        self.head.prev = cur
                    return
                else:
                    help_node = self.head
                    while cur.next != self.head:
                        # Found the element to delete
                        if cur.data == data:
                            help_node.next = cur.next
                            cur.next.prev = help_node
                            return
                        else:
                            help_node = cur
                            cur = cur.next

                    if cur.data == data:
                        help_node.next = cur.next
                        cur.next.prev = help_node
            except:
                print("there is no the %d in the linkedlist" % data)

    def delete_by_index(self, index):
        """ deletes a node in a location in the list"""

        global help_node
        cur = self.head
        length = self.get_length()
        if type(index) is int:
            if self.is_empty():
                return
            else:
                if index > length:
                    # The index value is out of range and prompts and exits
                    print("Index  is out of range.")
                    return
                else:
                    if index == 0:
                        # If the element of the first node is the element to be deleted
                        if cur.next == None:
                            self.head = None
                        else:
                            # If the linked list has more than one node
                            # First find the tail node, point the next node's next to the second node
                            while cur.next != self.head:
                                cur = cur.next
                            # cur pointed to the tail node
                            cur.next = self.head.next
                            self.head = self.head.next
                            self.head.prev = cur
                        return

                    else:
                        while (index) > 0:
                            if index == 1:
                                help_node = cur
                            cur = cur.next
                            index -= 1
                        help_node.next = cur.next
                        cur.next.prev = help_node
                        return
        else:
            print("Index value is not int.")
            return

    def update(self, value, index):
        """modifies the value for a node in a location in the list"""
        cur=self.head
        length = self.get_length()
        if type(index) is int:
            if index > length:
                # Index value is out of range and prompts and exits
                print("Index  is out of range.")
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    while cur.next !=self.head:
                        cur=cur.next
                    this_node.next = self.head.next
                    this_node.prev = self.head.prev
                    self.head.next.prev = this_node
                    cur.next = this_node
                    self.head = this_node
                else:
                    cur = self.head
                    while index - 1:
                        cur = cur.next
                        index -= 1
                    this_node.next = cur.next.next
                    cur.next.next.prev = this_node
                    cur.next = this_node
                    this_node.prev = cur
                    return
        else:
            print("Index value is not int.")
            return

    def clear_double_linkedlist(self):
        """Empty linked list"""
        self.head = None
        self.length = 0
        print("Clear the linked list finished.")
