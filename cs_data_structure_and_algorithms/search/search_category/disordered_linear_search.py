#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class OrderedLinearSearch():
    def __init__(self,array=[]):
        self.array = array

    def search(self,data):
        record_index = []
        for i in range(len(self.array)):
            if self.array[i] == data:
                record_index.append(i)

        return record_index

if __name__ =="__main__":
    a=[21,34,654,3,54,58,76,9,23,3]
    t = OrderedLinearSearch(a)
    print(t)
    print(t.search(3))