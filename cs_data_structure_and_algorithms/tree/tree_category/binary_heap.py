#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

# 二叉堆
class BinaryHeap(object):
    # 创建一个新的,空的二叉堆。
    def __init__(self):
        self.item_list = [0]  # 第0项元素代表堆中存放的实际元素的个数

    # 向堆添加一个新项。
    def insert(self, new_item):
        self.item_list.append(new_item)
        self.item_list[0] += 1  # 记录元素个数的增加self.upward_adjust(self.item_list[0]) #向上调整

    # 向上调整
    def upward_adjust(self, index):
        while index // 2 > 0:  # 父节点存在
            if self.item_list[index] < self.item_list[index//2]: #如果当前节点比父亲节点更小,则交换
                temp = self.item_list[index]
                self.item_list[index] = self.item_list[index//2]
                self.item_list[index//2] = temp
            index = index//2 #继续调整 else: #如果当前节点不比父节点小 break #停止调整

    # 返回具有最小键值的项,并将项留在堆中。
    def get_min(self):
        if self.item_list[0] > 0:  # 不为空,返回堆顶
            return self.item_list[1]
        else:
            return None

    # 返回具有最小键值的项,从堆中删除该项。
    def pop_min(self):
        if self.item_list[0] == 0:  # 如果为空,返回None
            return None
        else:
            top_min = self.item_list[1] #将堆顶元素
            self.item_list[1] = self.item_list[self.item_list[0]] #将最后一个元素移动到堆顶
            self.item_list[0] -= 1
            self.downward_adjust(1) #向下调整
        return top_min

    # 向下调整
    def downward_adjust(self, index):
        while 2 * index <= self.item_list[0]:  # 子节点存在
            if 2*index+1 <= self.item_list[0]: #左右子节点都存在
                if self.item_list[2*index]<self.item_list[2*index+1]: #左子节点更小
                    if self.item_list[index]>self.item_list[2*index]: #比左子节点更大,交换
                        temp = self.item_list[index]
                        self.item_list[index] = self.item_list[2*index]
                        self.item_list[2*index] = temp
                        index = 2*index #继续调整
                    else: #没有比子节点更大,停止调整
                        break
                else: #右子节点更小
                    if self.item_list[index]>self.item_list[2*index+1]: #比右子节点更大,交换
                        temp = self.item_list[index]
                        self.item_list[index] = self.item_list[2*index+1]
                        self.item_list[2*index+1] = temp
                        index = 2*index+1 #继续调整
                    else: #没有比子节点更大,停止调整
                        break
            else: #只存在左节点
                if self.item_list[index]>self.item_list[2*index]: #比左子节点更大,交换
                    temp = self.item_list[index]
                    self.item_list[index] = self.item_list[2*index]
                    self.item_list[2*index] = temp
                else: #没有比子节点更大,停止调整
                    break

    # 判断是否为空
    def isEmpty(self):
        return 0 == self.item_list[0]

    # 返回堆中的项数
    def size(self):
        return self.item_list[0]

    # 从列表构建一个新的堆。覆盖掉当前的堆
    def build_heap(self, input_list):
        self.item_list = [0] + input_list
        self.item_list[0] = len(input_list)
        for index in range(self.item_list[0] // 2, 0, -1):  # 从最后一个有叶节点的元素起逐个向下调整
            self.downward_adjust(index)

def main():
    bh = BinaryHeap()
    list_range= [9, 5, 6, 2, 3, 10, 4, 1, 8, 7, 0,34,4564,5676,879,768]
    t=bh.build_heap(list_range)
    for i in range(len(list_range)):
        print(bh.pop_min())
if __name__ == "__main__":
    main()
