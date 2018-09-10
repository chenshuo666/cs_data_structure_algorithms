#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class SecondaryDetectionMethod(object):

    def __init__(self, tablesize):
        self.elem = [None for i in range(tablesize)]  # 使用list数据结构作为哈希表元素保存方法
        self.count = tablesize  # 最大表长
        self.num_node = 0  # number of nodes in the map

    def hash_get_index(self, value):
        return value % self.count  # 散列函数采用除留余数法

    def get_item(self, value):
        """查找关键字，返回布尔值"""
        star = address = self.hash_get_index(value)
        while self.elem[address] != value:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star:  # 说明没找到或者循环到了开始的位置
                return False
        return True

    def insert(self, value):
        """插入关键字到哈希表内"""
        address = self.hash_get_index(value)  # 求散列地址
        if self.elem[address] is not None:  # 当前位置已经有数据了，发生冲突。
            for i in range(len(self.elem)):
                t = ( address + i**2 ) % self.count  # 线性探测下一地址是否可用
                if self.elem[t] is not None:
                    continue
                else:
                    self.elem[t] = value  # 没有冲突则直接保存。
        else:
            self.elem[address] = value
        self.num_node += 1

    def delete(self, value):
        for i in range(len(self.elem)):
            if self.elem[i] == value:
                self.elem[i] = None

if __name__ == '__main__':
    list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = SecondaryDetectionMethod(12)
    for i in list_a:
        hash_table.insert(i)

    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)), end=" ")
    print("\n")

    print(hash_table.get_item(15))
    print(hash_table.get_item(33))