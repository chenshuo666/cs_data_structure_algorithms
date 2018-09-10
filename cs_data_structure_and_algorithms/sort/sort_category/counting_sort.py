#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class CountingSort():
    def __init__(self):
        self.array = []

    def sort(self,lists):
        n = len(lists)
        sort_lists = [0 for i in range(n)]
        count_lists = [0 for i in range(max(lists)+1)]
        for i in lists:
            count_lists[i] += 1
        for i in range(1, len(count_lists)):
            count_lists[i] = count_lists[i - 1] + count_lists[i]#c中存放小于和等于i的数目
        for i in lists:
            sort_lists[count_lists[i] - 1] = i
            count_lists[i] -= 1
        return sort_lists

if __name__ == '__main__':
    a=[2, 5, 3, 0, 2, 3, 0, 3]
    #b=[0]*len(a)
    b=[None for i in range(len(a))]
    t=CountingSort()
    print(t.sort(a))