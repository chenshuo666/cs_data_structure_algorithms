#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class MergeSort(object):
    def __init__(self):
        self.array = []

    def mergesort(self,root):
        # 归并排序
        if len(root) <= 1:
            return root
        num = int(len(root) / 2)
        left = self.mergesort(root[:num])
        right = self.mergesort(root[num:])
        return self.sort(left,right)

    def sort(self,left,right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

if __name__=="__main__":
    mm = [3,2,5,7,23,6,87]
    print(MergeSort().mergesort(mm))
