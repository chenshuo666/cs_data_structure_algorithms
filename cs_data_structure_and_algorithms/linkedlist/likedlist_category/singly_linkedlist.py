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


class SinglyLinkedList:
    def __init__(self):
        """
        SinglyLinkedList 的初始化
        """
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
        cur = self._head
        if cur:
            i = 1
            while cur.next:
                cur = cur.next
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
            while cur != None:
                if cur.data == data:
                    print("the index of the %s is %s".format(data, j))
                    return True
                cur = cur.next
                j += 1
            return False

    def travel_print(self):
        """
        遍历整个链表，并输出链表的值
        """
        if self.is_empty():
            print("Linked list's length is 0")
        else:
            node = self._head
            print("_head -->", node.data, end=' ')
            while node.next:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def insert_append(self, this_node):

        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node)
        if self.is_empty():
            # 链表为空的情况将头指针指向当前node
            self._head = this_node
        else:
            node = self._head
            while node.next:
                node = node.next
            node.next = this_node
        self.length += 1

    def insert(self, value, index):
        """
        链表的插入操作
        :param value: 要插入的值
        :param index: 位置
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index value is out of range.")
                return
            else:
                # 获得当前node对象和_head
                this_node = Node(data=value)
                cur = self._head

                if index == 0:
                    # 索引值为0是将
                    self._head = this_node
                    this_node.next = cur
                    return

                while index - 1:
                    cur = cur.next
                    index -= 1
                # 将当前节点与后一个节点拆开，this_node指向后一个节点，前一个节点指向this_node
                this_node.next = cur.next
                cur.next = this_node
                self.length += 1
                return

        else:
            print("Index value is not int.")
            return


    def delete_node(self, index):
        """
        删除链表中某个位置的节点
        :param index: 位置索引
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    self._head = self._head.next
                else:
                    cur = self._head
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
        """为链表中某个位置的节点修改值"""

        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    this_node.next = self._head.next
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

    def get_value(self, index):
        """
        获取链表中某个位置节点的值
        :param index: 位置索引
        :return: 该节点值, int or not
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    return self._head.data
                else:
                    cur = self._head
                    while index - 1:
                        cur = cur.next
                        index -= 1
                    return cur.next.data
        else:
            print("Index value is not int.")
            return

    def clear_singly_linkedlist(self):
        """清空链表"""
        self._head = None
        self.length = 0
        print("Clear the linked list finished.")
