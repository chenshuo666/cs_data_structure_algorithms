#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class BruteForce():
    def __init__(self,arr1,arr2):
        self.array1 = arr1
        self.array2 = arr2

    def string_match(self):
        list_index = []
        m=len(self.array1)
        n= len(self.array2)
        for i in range(m - n + 1):
            index = i
            for j in range(len(self.array2)):
                if self.array1[index] == self.array2[j]:
                    index += 1

                if index - i == len(self.array2):
                    list_index.append(i)
        return list_index

if __name__ == "__main__":
    t = BruteForce("adbcbdc", "dc")
    print(t.string_match())