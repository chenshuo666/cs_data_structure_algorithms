#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class OrderedLinearSearch():
    def __init__(self,array=[]):
        self.array = array

    def search_up(self,data):
        record_index = []
        for i in range(len(self.array)):
            if self.array[i] == data:
                record_index.append(i)
            elif self.array[i] >data:
                return record_index


    def search_down(self,data):
        record_index = []
        for i in range(len(self.array)):
            if self.array[i] == data:
                record_index.append(i)
            elif self.array[i] < data:
                return record_index


    def search(self,data):
        index = []
        t = 0
        for i in range(1,len(self.array)):
            if self.array[i] >= self.array[i-1]:
                index.append(1)
            elif self.array[i] <= self.array[i-1]:
                index.append(0)
            else:
                return -1

        for i in range(len(index)):
            t = t +index[i]

        if t==len(index):
            return self.search_up(data)
        elif t == 0 :
            return self.search_down(data)
        else:
            return 0

if __name__ =="__main__":
    a=[21,34,654,34254,2313125,3634753476645,231554363265346456,54275356846484869856]
    t = OrderedLinearSearch(a)
    print(t.search(654))

