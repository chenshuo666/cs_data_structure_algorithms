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
        """Get the size of the stack """
        return self.height

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

    def push(self,node_instantiation):#Add to the stack
        if self.isStackFull() :
            print("the stack is full")
        else:
            node_instantiation=Node(node_instantiation)  #Instance node
            node_instantiation.next=self.top  #Top element passed value to a pointer
            self.top=node_instantiation
            self.height += 1
            return node_instantiation.data


    @property
    def pop(self):  #Popping
        if self.top == None:
            return None
        else:
            tmp=self.top.data
            self.top=self.top.next  #Move one down and proceed
            self.height -= 1
            return tmp

    def travel_print(self):
        """
        Traverse the entire stack and output the value of the stack
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
