#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class OneListStack():
    def __init__(self,size):
        self.dataArray = []
        self.size = size
        self.topOne = -1
        self.topTwo = size

    def push(self,stackID,data):
        if self.topTwo == self.topOne+1:
            print("two stacks are full")
            return 0
        if stackID == 1:
            self.topOne +=1
            self.dataArray[self.topOne] = data

        elif stackID == 2:
            self.topTwo-=1
            self.dataArray[self.topTwo] = data
        else:
            return 0

    def pop(self,stackID):
        if stackID == 1:
            if self.topOne == -1:
                print("First stack is empty")
                return None
            pop_data = self.dataArray[self.topOne]
            self.dataArray[self.topOne] = None
            self.topOne -= 1
            return pop_data
        elif stackID == 2:
            if self.topTwo == self.size :
                print("Second stack is empty")
                return None
            pop_data = self.dataArray[self.topTwo]
            self.dataArray[self.topTwo] = None
            self.topTwo +=1
            return pop_data
        else:
            return None

    def get_top(self,stackID):
        if stackID == 1:
            if self.topOne == -1:
                print("First stack is empty")
                return None
            else:
                return self.dataArray[self.topOne]

        elif stackID == 2:
            if self.topTwo == self.size:
                print("Second stack is empty")
                return None
            else:
                return self.dataArray[self.topTwo]
        else:
            return None

    def isEmpty(self,stackID):
        if stackID == 1:
            if self.topOne == -1:
                print("First stack is empty")
                return True
            else:
                return False

        if stackID == 1:
            if self.topTwo == self.size:
                print("Second stack is empty")
                return True
            else:
                return False




