#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class SelectionSort(object):
    def __init__(self,array = []):
        self.array = array
    def sort(self):
        global min
        for i in range(len(self.array)):
            min = i
            for j in range(i+1,len(self.array)):
                if self.array[min] > self.array[j]:
                    min = j
            self.array[i], self.array[min] = self.array[min], self.array[i]

        return self.array
if __name__=="__main__":
    mm = [3,2,5,7,23,6,8,5,3,6,9,89,65,78,0,6,4,5,8,54,7,891,2,4,6,6,345]
    t=SelectionSort(mm)
    print(t.sort())