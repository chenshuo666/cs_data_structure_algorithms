#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class BoyceMoore():
    def __init__(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def invert(self):
        self.arr1 = self.arr1[::-1]
        self.arr2 = self.arr2[::-1]

    def boyce_moore_match(self):
        self.invert()
        m = len(self.arr1)
        n = len(self.arr2)
        cur = 0
        table = self.partial_table(self.arr2)
        while cur <= m - n:
            for i in range(n):
                if self.arr1[i + cur] != self.arr2[i]:
                    cur += max(i - table[i - 1], 1)
                    break
            else:
                return True
        return False

    def partial_table(self,p):
        prefix = set()
        ret = [0]
        for i in range(1, len(p)):
            prefix.add(p[:i])
            postfix = {p[j:i + 1] for j in range(1, i + 1)}
            ret.append(len((prefix & postfix or {''}).pop()))
        return ret

if __name__ =="__main__":
    t=BoyceMoore("BBC ABCDAB ABCDABCDABDE", "ABCDABD")
    print(t.boyce_moore_match())