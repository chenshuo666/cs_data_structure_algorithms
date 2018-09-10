#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedListStack(object):
    def __init__(self,max_capacity):
        self.top=None
        self.max_capacity = max_capacity
        self.height = 0

    def get_top(self):
        if self.top!=None:
            return self.top.data
        else:
            return None

    def get_height(self):
        """获取栈的大小"""
        return self.height
        # current_node = self.top
        # if current_node:
        #     i = 1
        #     while current_node.next:
        #         current_node = current_node.next
        #         i += 1
        #     return i
        # else:
        #     return 0

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def isStackFull(self):
        if self.get_height()==self.max_capacity:
            return True
        else:
            return False

    def push(self,node_instantiation):#添加到栈中
        if self.isStackFull() :
            print("the stack is full")
        else:
            node_instantiation=Node(node_instantiation)  #实例化节点
            node_instantiation.next=self.top  #顶端元素传值给一个指针
            self.top=node_instantiation
            self.height += 1
            return node_instantiation.data


    @property
    def pop(self):  #出栈
        if self.top == None:
            return None
        else:
            tmp=self.top.data
            self.top=self.top.next  #下移一位，进行
            self.height -= 1
            return tmp

    def travel_print(self):
        """
        遍历整个栈，并输出栈的值
        """
        if self.isEmpty():
            print("Stack's height is 0")
        else:
            node = self.top
            print("top -->", node.data, end=' ')
            while node.next:
                node = node.next
                print("-->", node.data, end=' ')
            print(" ")

    def clear_linkedlist_stack(self):
        self.top = None
        self.height = 0
        print("the stack is empty")
