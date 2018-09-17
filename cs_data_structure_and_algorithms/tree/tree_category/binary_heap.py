#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

class BinaryHeap(object):
    def __init__(self):
        self.item_list = [0]  # The 0th element represents the number of actual elements stored in the heap


    def insert(self, new_item):
        """Add a new item to the heap"""
        self.item_list.append(new_item)
        self.item_list[0] += 1
        self.upward_adjust(self.item_list[0])


    def upward_adjust(self, index):
        """Adjust upward"""
        # Parent node exists
        while index // 2 > 0:
            #Exchange if the current node is smaller than the parent node
            if self.item_list[index] < self.item_list[index//2]:
                temp = self.item_list[index]
                self.item_list[index] = self.item_list[index//2]
                self.item_list[index//2] = temp
            index = index//2 #Continue to adjust, if the current node is not smaller
                            # than the parent node, stop adjusting


    def get_min(self):
        """Get the min element of the heap"""
        if self.item_list[0] > 0:  # Not empty, return to the top of the heap
            return self.item_list[1]
        else:
            return None


    def pop_min(self):
        """Returns the item with the smallest key value, removing the item from the heap"""
        if self.item_list[0] == 0:  # If it is empty, return None
            return None
        else:
            top_min = self.item_list[1]
            self.item_list[1] = self.item_list[self.item_list[0]] #Move the last element to the top of the heap
            self.item_list[0] -= 1
            self.downward_adjust(1) # Adjust downward
        return top_min


    def downward_adjust(self, index):
        """Adjust downward"""
        while 2 * index <= self.item_list[0]:
            if 2*index+1 <= self.item_list[0]:
                if self.item_list[2*index]<self.item_list[2*index+1]:
                    if self.item_list[index]>self.item_list[2*index]:
                        temp = self.item_list[index]
                        self.item_list[index] = self.item_list[2*index]
                        self.item_list[2*index] = temp
                        index = 2*index
                    else:
                        break
                else:
                    if self.item_list[index]>self.item_list[2*index+1]:
                        temp = self.item_list[index]
                        self.item_list[index] = self.item_list[2*index+1]
                        self.item_list[2*index+1] = temp
                        index = 2*index+1
                    else:
                        break
            else:
                if self.item_list[index]>self.item_list[2*index]:
                    temp = self.item_list[index]
                    self.item_list[index] = self.item_list[2*index]
                    self.item_list[2*index] = temp
                else:
                    break


    def isEmpty(self):
        """judge whether the heap is empty"""
        return 0 == self.item_list[0]


    def size(self):
        """get the number of element of the heap"""
        return self.item_list[0]

    def build_heap(self, input_list):
        """build a new heap , delete old heap"""
        self.item_list = [0] + input_list
        self.item_list[0] = len(input_list)
        for index in range(self.item_list[0] // 2, 0, -1):
            self.downward_adjust(index)

def main():
    bh = BinaryHeap()
    list_range= [9, 5, 6, 2, 3, 10, 4, 1, 8, 7, 0,34,4564,5676,879,768]
    t=bh.build_heap(list_range)
    for i in range(len(list_range)):
        print(bh.pop_min())
if __name__ == "__main__":
    main()
