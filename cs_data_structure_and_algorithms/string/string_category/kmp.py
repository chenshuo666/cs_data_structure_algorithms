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
        cur = 0  # 起始指针cur
        table = self.partial_table(self.arr2)
        while cur <= m - n:
            for i in range(n):
                if self.arr1[i + cur] != self.arr2[i]:
                    cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                    break
            else:
                return True
        return False

    # 部分匹配表
    def partial_table(self,p):
        '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
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