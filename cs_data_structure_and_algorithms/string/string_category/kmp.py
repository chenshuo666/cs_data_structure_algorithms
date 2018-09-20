#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class KMP():
    def __init__(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    # KMP
    def kmp_match(self):
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
        postfix = set()
        ret = [0]
        for i in range(1, len(p)):
            prefix.add(p[:i])
            postfix = {p[j:i + 1] for j in range(1, i + 1)}
            ret.append(len((prefix & postfix or {''}).pop()))
        return ret

if __name__ =="__main__":
    t=KMP("BBC ABCDAB ABCDABCDABDE", "ABCDABD")
    print(t.kmp_match())