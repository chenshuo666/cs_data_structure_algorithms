#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class InsertionSort(object):
    def __init__(self,array = []):
        self.array = array
    def sort(self):
        for i in range(1,len(self.array)):
            key = self.array[i]
            j=i-1
            while j >= 0:
                if key < self.array[j]:
                    self.array[j+1] = self.array[j]
                    self.array[j] = key
                j-=1
        return self.array
if __name__=="__main__":
    mm = [3,2,5,7,23,6,8,5,3,6,9,89,65,78,0,6,4,5,8,54,7,891,2,4,6,6,345]
    t=InsertionSort(mm)
    print(t.sort())