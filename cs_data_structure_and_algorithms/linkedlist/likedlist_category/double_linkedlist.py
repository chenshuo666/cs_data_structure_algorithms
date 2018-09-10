#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

"""Initialize the node, the node includes the currently stored content and a pointer to the next node"""

class Node(object):
    """双向链表节点"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return str(self.data)


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self):
        self.length=0
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
            while current_node.next:
                current_node = current_node.next
                i += 1
            return i
        else:
            return 0

    def get_data_by_index(self,index):
        j = 0
        p = self._head
        if self.is_empty():
            print('Linklist is empty.')
            return

        else:

            while p.next!=0 and j <index:
                p = p.next
                j+=1
            if j ==index:
                return p.data
            else:
                print('Target is not exist!')

    def get_data_by_self(self, data):
        """查找元素是否存在"""
        cur = self._head
        j=0
        if self.is_empty():
            print('Linklist is empty.')
            return

        else:
            while cur != None:
                if cur.data == data:
                    print("the index of the %d is %d" % (data,j))
                    return True
                cur = cur.next
                j+=1
            return False

    def travel_print(self):
        """遍历链表"""
        if self.is_empty():
            print("Linked list's length is 0")
        else:
            node = self._head
            print("head -->", node.data, end=' ')
            while node.next:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def insert_head(self, data):
        """头部插入元素"""
        node = Node(data)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def insert_append(self, data):
        """尾部插入元素"""
        node = Node(data)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

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
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def delete_by_data(self, data):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.data == data:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.data == data:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

    def delete_by_index(self, index):
        """删除链表中某个位置的节点"""

        cur = self._head

        length=self.get_length()
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
                        if cur.next == None:
                            self._head = None
                        else:
                            cur.next.prev = None
                            self._head = cur.next
                        return
                    else:
                        while (index) > 0:
                            cur = cur.next
                            index -= 1

                        # 将cur的前一个节点的next指向cur的后一个节点
                        cur.prev.next = cur.next
                        # 将cur的后一个节点的prev指向cur的前一个节点
                        cur.next.prev = cur.prev
                        length -= 1
                        return
        else:
            print("Index value is not int.")
            return

    def update(self, value, index):
        """为链表中某个位置的节点修改值"""

        length = self.get_length()
        if type(index) is int:
            if index > length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    this_node.next = self._head.next
                    this_node.prev =None
                    self._head = this_node
                else:
                    cur = self._head
                    while index - 1:
                        cur = cur.next
                        index -= 1
                    this_node.next = cur.next.next
                    this_node.prev = cur.next.prev
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
