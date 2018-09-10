#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class ShellSort(object):
    def __init__(self,array = []):
        self.array = array

    def sort(self):
        group_len = int(len(self.array) / 2)
        while group_len > 0:
            for i in range(0, group_len):
                j = i + group_len
                while j < len(self.array):
                    k = j - group_len
                    key = self.array[j]
                    while k >= 0:
                        if self.array[k] > key:
                            self.array[k + group_len] = self.array[k]
                            self.array[k] = key
                        k -= group_len
                    j += group_len
            group_len = int(group_len/2)
        return self.array

if __name__=="__main__":
    mm = [3,2,5,7,23,6,8,5,3,6,9,89,65,78,0,6,4,5,8,54,7,891,2,4,6,6,345]
    t=ShellSort(mm)
    print(t.sort())