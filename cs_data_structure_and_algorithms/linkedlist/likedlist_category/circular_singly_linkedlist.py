#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

"""Initialize the node, the node includes the currently stored content and a pointer to the next node"""


class Node(object):
    """双向链表节点"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class CircularSinglyLinkList(object):
    """双向链表"""

    def __init__(self):
        self.length = 0
        self._head = None

    def is_empty(self):
        """
        判断该链表是否为空
        """
        if self._head == None:
            return True
        else:
            return False

    def get_length(self):
        """
        获取链表长度
        """
        current_node = self._head
        if current_node:
            i = 1
            while current_node.next != self._head:
                current_node = current_node.next
                i += 1
            return i
        else:
            return 0

    def get_data_by_index(self, index):
        j = 0
        p = self._head
        if self.is_empty():
            print('Linklist is empty.')
            return
        else:

            while p.next != 0 and j < index:
                p = p.next
                j += 1
            if j == index:
                return p.data
            else:
                print('Target is not exist!')

    def get_data_by_self(self, data):
        """查找元素是否存在"""
        cur = self._head
        j = 0
        if self.is_empty():
            print('Linklist is empty.')
            return
        else:
            while cur.next!= self._head:
                if cur.data == data:
                    print("the index of the %d is %d" % (data, j))
                    return True
                cur = cur.next
                j += 1
            return False

    def travel_print(self):
        """遍历链表"""
        if self.is_empty():
            print("Linked list's length is 0")
        else:
            node = self._head
            print("head -->", node.data, end=' ')
            while node.next !=self._head:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def insert_head(self, data):
        """头部插入元素"""
        node = Node(data)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            #添加的节点指向_head
            node.next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            #_head指向添加node的
            self._head = node

    def insert_append(self, data):
        """尾部插入元素"""
        node = Node(data)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next=self._head

    def insert(self, pos, data):
        """在指定位置添加节点"""
        if pos <= 0:
            self.insert_head(data)
        elif pos > (self.get_length() - 1):
            self.insert_append(data)
        else:
            node = Node(data)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def delete_by_data(self, data):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            try:
                if cur.data == data:
                    # 如果首节点的元素即是要删除的元素
                    if cur.next == None:
                        self._head = None
                    else:
                        # 如果链表不止一个节点
                        # 先找到尾节点，将尾节点的next指向第二个节点
                        while cur.next != self._head:
                            cur = cur.next
                        # cur指向了尾节点
                        cur.next = self._head.next
                        self._head = self._head.next
                    return
                else:
                    help_node = self._head
                    while cur.next != self._head:
                        # 找到了要删除的元素
                        if cur.data == data:
                            help_node.next = cur.next
                            return
                        else:
                            help_node = cur
                            cur = cur.next

                    if cur.data == data:
                        help_node.next = cur.next
            except:
                print("there is no the %d in the lined list." % data)

    def delete_by_index(self, index):
        """删除链表中某个位置的节点"""

        global help_node
        cur = self._head
        length = self.get_length()
        if type(index) is int:
            if self.is_empty():
                return
            else:
                if index > length:
                    # 索引值超出范围直接提示并且退出
                    print("Index  is out of range.")
                    return
                else:
                    if index == 0:
                        # 如果首节点的元素即是要删除的元素
                        if cur.next == None:
                            self._head = None
                        else:
                            # 如果链表不止一个节点
                            # 先找到尾节点，将尾节点的next指向第二个节点
                            while cur.next != self._head:
                                cur = cur.next
                            # cur指向了尾节点
                            cur.next = self._head.next
                            self._head = self._head.next
                        return

                    else:
                        while (index) > 0:
                            if index == 1:
                                help_node = cur
                            cur = cur.next
                            index -= 1
                        help_node.next = cur.next
                        return
        else:
            print("Index value is not int.")
            return

    def update(self, value, index):
        """为链表中某个位置的节点修改值"""

        cur=self._head
        length = self.get_length()
        if type(index) is int:
            if index > length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    while cur.next !=self._head:
                        cur=cur.next
                    this_node.next = self._head.next
                    cur.next = this_node
                    self._head = this_node
                else:
                    cur = self._head
                    while index - 1:
                        cur = cur.next
                        index -= 1
                    this_node.next = cur.next.next
                    cur.next = this_node
                    return
        else:
            print("Index value is not int.")
            return

    def clear_double_linkedlist(self):
        """清空链表"""
        self._head = None
        self.length = 0
        print("Clear the linked list finished.")

