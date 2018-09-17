#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from queue_category.simply_array_queue import SimplyArrayQueue

class KReverseQueue():
    def __init__(self,queue,k):
        self.k = k
        self.queue = queue

    def reverse(self):
        a = []
        j = 0
        n = self.queue.length - 1
        n1 = self.queue.length - 1
        m = self.queue.length-1-self.k
        if self.queue.isEmpty != True:
            for i in range(self.queue.length):
                a.append(self.queue.dequeue())

        while j <= m:
            self.queue.enqueue(a[j])
            j += 1

        while n <= n1 and n > m:
            self.queue.enqueue(a[n])
            n -= 1

        return self.queue

if __name__ == "__main__":
    l1 = SimplyArrayQueue(20)
    for i in range(4):
        l1.enqueue(i)

    l1.travel_print()
    m = KReverseQueue(l1,2)
    m.reverse()
    l1.travel_print()


