#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from queue_category.simply_array_queue import SimplyArrayQueue

class ReverseQueue():
    def __init__(self,queue):
        self.queue = queue

    def reverse(self):
        a = []
        j = self.queue.length-1
        if self.queue.isEmpty != True:
            for i in range(self.queue.length):
                a.append(self.queue.dequeue())

        while j >= 0:
            self.queue.enqueue(a[j])
            j -= 1

        return self.queue

if __name__ == "__main__":
    l1 = SimplyArrayQueue(10)
    for i in range(5):
        l1.enqueue(i)

    l1.travel_print()
    m = ReverseQueue(l1)
    m.reverse()
    print(l1.travel_print())


