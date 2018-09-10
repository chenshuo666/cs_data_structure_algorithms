#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class BucketSort():
    def __init__(self):
        self.array = []
    def sort(self,lists):

        bucket = [0] * (max(lists) + 1)
        for i in lists:
            bucket[i] += 1

        sort_lists = []
        for j in range(len(bucket)):
            if bucket[j] != 0:
                for y in range(bucket[j]):
                    sort_lists.append(j)

        return sort_lists

if __name__ == '__main__':
    a=[2, 5, 3, 0, 2, 3, 0, 3,34,564,5,8776,85,142]
    t=BucketSort()
    print(t.sort(a))