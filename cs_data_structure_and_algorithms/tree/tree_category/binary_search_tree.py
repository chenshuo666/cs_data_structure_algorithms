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


    def search(self, root, parent, data):
        """Recursive search"""
        if root is None:
            return False, root, parent
        if root.data == data:
            return True, root, parent
        if root.data > data:
            return self.search(root.left, root, data)
        else:
            return self.search(root.right, root, data)

    def insert(self, data):
        """insert data to the tree"""
        node = Node(data)
        if self.root is None:
            self.root = node

        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            if data > p.data:
                p.right= node
            else:
                p.left = node

    def delete(self, root, data):
        """delete data from the tree"""
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
            else:  # Left and right subtrees are not empty
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


    def preorder(self,root):
        if root is None:
            return []
        result = [root.data]
        left_data = self.preorder(root.left)
        right_data = self.preorder(root.right)
        return result + left_data + right_data

    def inorder(self,root):
        if root is None:
            return []
        result = [root.data]
        left_data = self.inorder(root.left)
        right_data = self.inorder(root.right)
        return left_data + result + right_data

    def postorder(self,root):
        if root is None:
            return []
        result = [root.data]
        left_data = self.postorder(root.left)
        right_data = self.postorder(root.right)
        return left_data + right_data + result

            
if __name__ == '__main__':

    Tree = BinarySearchTree()
    for i in range(20):
        Tree.insert(i)
    print(Tree.inorder(Tree.root))
    
    Tree.delete(Tree.root, 9)
    print(Tree.inorder(Tree.root))