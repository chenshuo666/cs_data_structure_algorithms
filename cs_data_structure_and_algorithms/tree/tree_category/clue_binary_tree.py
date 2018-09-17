#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node:
    def __init__(self,data):
        self.left = None
        self.ltag = 0
        self.data = data
        self.rtag = 0
        self.right = None

class ClueBinaryTree(object):
    def __init__(self):
        self.root = None
        self.node_number = 0

    def add(self, data):
        """create complete binary tree"""
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def preorder(self,root):  # 先序遍历
        if root is None:
            return []
        result = [root]
        left_data = self.preorder(root.left)
        right_data = self.preorder(root.right)
        return result + left_data + right_data

    def preorder_add_tag(self,root):
        node_list = self.preorder(root)
        for i in range(len(node_list)):
            if node_list[i].left is not None and node_list[i].right is not None:
                node_list[i].ltag = 0
                node_list[i].rtag = 1
            elif node_list[i].left is None and node_list[i].right is not None:
                node_list[i].ltag = 1
                node_list[i].rtag = 0
            elif node_list[i].right is None and node_list[i].left is not None:
                node_list[i].ltag = 0
                node_list[i].rtag = 1
            elif node_list[i].left is None and node_list[i].right is None:
                node_list[i].ltag = 1
                node_list[i].rtag = 1
        return node_list

    def inorder(self,root):
        if root is None:
            return []
        result = [root]
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return left + result + right

    def inorder_add_tag(self,root):
        node_list = self.inorder(root)
        for i in range(len(node_list)):
            if node_list[i].left is not None and node_list[i].right is not None:
                node_list[i].ltag = 0
                node_list[i].rtag = 1
            elif node_list[i].left is None and node_list[i].right is not None:
                node_list[i].ltag = 1
                node_list[i].rtag = 0
            elif node_list[i].right is None and node_list[i].left is not None:
                node_list[i].ltag = 0
                node_list[i].rtag = 1
            elif node_list[i].left is None and node_list[i].right is None:
                node_list[i].ltag = 1
                node_list[i].rtag = 1
        return node_list

    def postorder(self,root):  # 后序遍历
        if root is None:
            return []
        result = [root]
        left_data = self.postorder(root.left)
        right_data = self.postorder(root.right)
        return left_data + right_data + result

    def postorder_add_tag(self,root):
        node_list = self.postorder(root)
        for i in range(len(node_list)):
            if node_list[i].left is not None and node_list[i].right is not None:
                node_list[i].ltag = 0
                node_list[i].rtag = 1
            elif node_list[i].left is None and node_list[i].right is not None:
                node_list[i].ltag = 1
                node_list[i].rtag = 0
            elif node_list[i].right is None and node_list[i].left is not None:
                node_list[i].ltag = 0
                node_list[i].rtag = 1
            elif node_list[i].left is None and node_list[i].right is None:
                node_list[i].ltag = 1
                node_list[i].rtag = 1
        return node_list


if __name__ == "__main__":
    t = ClueBinaryTree()
    for i in range(12):
        t.add(i)
    m = t.postorder_add_tag(t.root)
    for i in range(len(m)):
        print(m[i].ltag,"----",m[i].data,"----",m[i].rtag)

