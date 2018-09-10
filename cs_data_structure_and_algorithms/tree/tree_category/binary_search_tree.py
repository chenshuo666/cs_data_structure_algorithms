#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 递归搜索
    def search(self, root, parent, data):
        if root is None:
            return False, root, parent
        if root.data == data:
            return True, root, parent
        if root.data > data:
            return self.search(root.left, root, data)
        else:
            return self.search(root.right, root, data)

    # 插入
    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node

        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            if data > p.data:
                p.right= node
            else:
                p.left = node

    # 删除
    def delete(self, root, data):
        flag, node, parent = self.search(root, root, data)
        if flag is False:
            print("There is no the data , delete fail!")
        else:
            if node.left is None:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right= node.right
                del parent
            elif node.right is None:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right= node.left
                del parent
            else:  # 左右子树均不为空
                pre = node.right
                if pre.left is None:
                    node.data = pre.data
                    node.right= pre.right
                    del pre
                else:
                    next = pre.left
                    while next.left is not None:
                        pre = next
                        next = next.left
                    node.data = next.data
                    pre.left = next.right
                    del parent


    def preorder(self,root):  # 先序遍历
        if root is None:
            return []
        result = [root.data]
        left_data = self.preorder(root.left)
        right_data = self.preorder(root.right)
        return result + left_data + right_data

    def inorder(self,root):  # 中序序遍历
        if root is None:
            return []
        result = [root.data]
        left_data = self.inorder(root.left)
        right_data = self.inorder(root.right)
        return left_data + result + right_data

    def postorder(self,root):  # 后序遍历
        if root is None:
            return []
        result = [root.data]
        left_data = self.postorder(root.left)
        right_data = self.postorder(root.right)
        return left_data + right_data + result

            
if __name__ == '__main__':

    BinarySearchTree = BinarySearchTree()  # 创建二叉查找树
    for i in range(20):
        BinarySearchTree.insert(i)
    print(BinarySearchTree.inorder(BinarySearchTree.root))  # 中序遍历
    
    BinarySearchTree.delete(BinarySearchTree.root, 9)
    print(BinarySearchTree.inorder(BinarySearchTree.root))