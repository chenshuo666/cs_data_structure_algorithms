#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node:
    """Node"""
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Initialize the binary tree"""
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

    def strict_binary_tree(self):
        """Judge strict binary tree"""
        if self.root is None:
            return None
        node_array = [self.root]
        count=0
        while node_array != []:
            pop_node = node_array.pop(0)
            if pop_node.left is not None:
                node_array.append(pop_node.left)
            if pop_node.right is not None:
                node_array.append(pop_node.right)

            if ((pop_node.left is not None ) and (pop_node.right is not None)) or \
                    ((pop_node.left is None) and (pop_node.right is None)):
                count += 1

        if count == self.node_number:
            return True
        else:
            return False

    def full_binary_tree(self):
        """judge full binary tree"""
        count  = self.get_height(self.root)
        n = self.get_node_number()
        if n == (2^count)-1:
            return True
        else:
            return False

    def complete_binary_tree(self):
        """judge complete binary tree"""
        if not self.root:
            return False
        node_array = [self.root]
        flag = False # Whether to activate the judgment process
        while node_array != []:
            pop_node = node_array.pop(0)

            if pop_node.left is not None:
                node_array.append(pop_node.left)
            if pop_node.right is not None:
                node_array.append(pop_node.right)

            if (not pop_node.left) and pop_node.right:  # Left empty, right not empty must not be CBT
                return False

            if flag:  # If the process is activated, determine if the node is a leaf node.
                if pop_node.left or pop_node.right:
                    return False

            if not (pop_node.left and pop_node.right):  # Left not empty, right empty | left empty, right empty
                flag = True  # The node after the activation judgment must be a leaf node

        return True

    def balanced_binary_tree(self,root):
        """Determine if it is a balanced binary tree"""
        if not root:
            return True
        leftheight = self.get_height(root.left)
        rightheight = self.get_height(root.right)
        if abs(leftheight - rightheight) > 1:
            return False
        return self.balanced_binary_tree(root.left) and self.balanced_binary_tree(root.right)

    def get_height(self,root):
        """Get the height of the tree"""
        if root is None:
            return 0
        else:
            leftheight = self.get_height(root.left)
            rightheight = self.get_height(root.right)
        if (leftheight > rightheight):
            return (leftheight+1)
        else:
            return (rightheight+1)

    def get_data_by_self(self,root,data):
        """Determine if there is a node by data"""
        if root == None:
            return False
        else:
            if data == root.data:
                return True
            else:
                bool = self.get_data_by_self(root.right,data)
                if bool == True:
                    return bool
                else:
                    return(self.get_data_by_self(root.left, data))


    def get_node_number(self):
        """Get the num of all nodes"""
        return self.node_number

    def hierarchicalorder(self):
        """Hierarchical traversal"""
        if self.root is None:
            return None
        else:
            self.node_number = 1
            node_array = [self.root]
            res = [self.root.data]
            while node_array != []:
                pop_node = node_array.pop(0)
                if pop_node.left is not None:
                    node_array.append(pop_node.left)
                    res.append(pop_node.left.data)
                    self.node_number  +=1

                if pop_node.right is not None:
                    node_array.append(pop_node.right)
                    res.append(pop_node.right.data)
                    self.node_number += 1
        return res

    def preorder(self,root):
        """Pre-order traversal"""
        if root is None:
            return []
        result = [root.data]
        left_data = self.preorder(root.left)
        right_data = self.preorder(root.right)
        return result + left_data + right_data

    def inorder(self,root):
        """In-order traversal"""
        if root is None:
            return []
        result = [root.data]
        left_data = self.inorder(root.left)
        right_data = self.inorder(root.right)
        return left_data + result + right_data

    def postorder(self,root):
        """Post-order traversal"""
        if root is None:
            return []
        result = [root.data]
        left_data = self.postorder(root.left)
        right_data = self.postorder(root.right)
        return left_data + right_data + result

    def clear_tree(self):
        """Empty the tree"""
        self.root = None
        self.node_number = 0
        print("the tree is empty!")

if __name__ == "__main__":
    t = BinaryTree()
    for i in range(12):
        t.add(i)
    # print('层序遍历:', t.hierarchicalorder())
    # print('先序遍历:', t.preorder(t.root))
    # print('中序遍历:', t.inorder(t.root))
    # print('后序遍历:', t.postorder(t.root))
    # print(t.get_height(t.root))
    # print(t.node_number)
    # print(t.strict_binary_tree())
    # print(t.full_binary_tree())
    # print(t.complete_binary_tree())
    # print(t.balanced_binary_tree(t.root))
    # print(t.get_data_by_self(t.root,13))
    t.clear_tree()
    print('层序遍历:', t.hierarchicalorder())
