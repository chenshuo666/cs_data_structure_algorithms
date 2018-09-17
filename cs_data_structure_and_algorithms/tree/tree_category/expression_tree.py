#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=root

    def insertLeft(self,data):
        node = Node(data)
        if self.left==None:
            self.left=node
        else:
            node=Node(data)
            node.left=self.left
            self.left=node

    def insertRight(self,data):
        node = Node(data)
        if self.right==None:
            self.right=node
        else:
            node=Node(data)
            node.right=self.right
            self.right=node

def build_expressionTree_inorder(exp):
    tree=BinaryTree('')
    stack=[]
    stack.append(tree)
    currentTree=tree
    for i in exp:
        if i=='(':
            currentTree.insertLeft('')
            stack.append(currentTree)
            currentTree=currentTree.left
        elif i not in '+-*/()':
            currentTree.data=int(i)
            parent=stack.pop()
            currentTree=parent
        elif i in '+-*/':
            currentTree.data=i
            currentTree.insertRight('')
            stack.append(currentTree)
            currentTree=currentTree.right
        elif i==')':
            currentTree=stack.pop()
        else:
            raise ValueError
    return stack

def build_expressionTree_postorder(exp):
    stack=[]
    oper='+-*/'
    for i in exp:
        if i not in oper:
            tree=Node(i)
            stack.append(tree)
        else:
            right=stack.pop()
            left=stack.pop()
            tree=Node(i)
            tree.left=left
            tree.right=right
            stack.append(tree)
    return stack

if __name__ == "__main__":
    print(build_expressionTree_postorder('123*+2/'))