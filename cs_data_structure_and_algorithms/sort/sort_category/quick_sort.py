#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class QuickSort(object):
    def __init__(self,array = []):
        self.array = array

    def sort(self, lists, left, right):

        if left >= right:
            return lists
        key = lists[left]
        i = left
        j = right
        while left < right:
            while left < right and lists[right] >= key:
                right -= 1
            lists[left] = lists[right]
            while left < right and lists[left] <= key:
                left += 1
            lists[right] = lists[left]
        lists[right] = key
        self.sort(lists, i, left - 1)
        self.sort(lists, left + 1, j)

        return lists
if __name__=="__main__":
    mm = [3,2,5,7,2,23]
    t=QuickSort()
    print(t.sort(mm,0,len(mm)-1))