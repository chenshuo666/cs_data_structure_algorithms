#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class BruteForce(object):
    def __init__(self,arr1,arr2):
        self.array1 = arr1
        self.array2 = arr2

    def string_match(self):
        # 蛮力法字符串匹配
        m=len(self.array1)
        n=len(self.array2)
        for i in range(m - n + 1):
            index = i  # index指向下一个待比较的字符
            for j in range(len(self.array2)):
                if self.array1[index] == self.array2[j]:
                    index += 1
                else:
                    break
                if index - i == len(self.array2):
                    return i
        return -1

if __name__ == "__main__":
    t = BruteForce("adbcbdc", "dc")
    print(t.string_match())