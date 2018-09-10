#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import math
class RadixSort():
    def __init__(self):
        self.array = []

    def sort(self,lists, radix=10):

        k = int(math.ceil(math.log(max(lists), radix)))#获取列表中最大数的位数
        bucket = [[] for i in range(radix)]#构建10个桶
        for i in range(1, k + 1): # K次循环
            for j in lists:
                bucket[int(j / (radix ** (i - 1)) % (radix ** i))].append(j)# 析取整数第K位数字 （从低到高）
            del lists[:]
            for z in bucket:
                lists += z
                del z[:]
        return lists

if __name__ == '__main__':
    a=[21, 52, 31, 10, 25, 33, 7, 91]
    t=RadixSort()
    print(t.sort(a))