#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class BubbleSort(object):
    def __init__(self,array = []):
        self.array = array
    def sort(self):
        for i in range(len(self.array)):
            for j in range(i,len(self.array)):
                if self.array[i] > self.array[j]:
                    self.array[i], self.array[j] = self.array[j], self.array[i]

        return self.array
if __name__=="__main__":
    mm = [3,2,5,7,23,6,8,5,3,6,9,89,65,78,0,6,4,5,8,54,7,891,2,4,6,6,345]
    t=BubbleSort(mm)
    print(t.sort())