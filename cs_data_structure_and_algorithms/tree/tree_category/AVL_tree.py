#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

class Node:
    def __init__(self):
        self.left = None
        self.left_height = 0
        self.right = None
        self.right_height = 0
        self.data = None

class BalancedBinaryTree(object):
    def __init__(self):
        self.root = None
        self.front_list = []
        self.middle_list = []
        self.after_list = []


    def create_tree(self, n=0, l=()):
        """Generating a binary tree"""
        if l == []:
            print("The incoming list is empty")
            return
        if n > len(l) - 1:
            print("Generating a binary tree")
            return
        node = Node()
        node.data = l[n]
        if not self.root:
            self.root = node
            self.list = l
        else:
            self.add(self.root, node)
        self.create_tree(n + 1, l)


    def add(self, parent, new_node):
        """add node"""
        if new_node.data > parent.data:
            # The inserted value is larger than the parent value, so on the right side of the parent node
            if parent.right == None:
                parent.right = new_node
                # The height of the parent node of the newly inserted node is 1, that is, the child height value is 0+1.
                parent.right_height = 1
                # After inserting the value, update the height of the node from bottom to top.
            else:
                self.add(parent.right, new_node)
                # The right height of the father node is equal to the right child,
                # the larger of the left and right heights + 1
                parent.right_height = max(parent.right.right_height, parent.right.left_height) + 1
                # Start to judge the balanced binary tree here
                # The height on the right is greater than the height on the left.
                if parent.right_height - parent.left_height >= 2:
                    self.right_avertence(parent)
        else:
            # The inserted value is smaller than the parent value, so on the left side of the parent node
            if parent.left == None:
                parent.left = new_node
                parent.left_height = 1
            else:
                self.add(parent.left, new_node)
                parent.left_height = max(parent.left.right_height, parent.left.left_height) + 1
                # Start to judge the balanced binary tree here
                # The height on the left is greater than the height on the right.
                if parent.left_height - parent.right_height >= 2:
                    self.left_avertence(parent)

    def get_height(self, root):
        """get height of the AVL tree"""
        if root is None:
            return 0
        else:
            leftheight = self.get_height(root.left)
            rightheight = self.get_height(root.right)
        if (leftheight > rightheight):
            return (leftheight + 1)
        else:
            return (rightheight + 1)

    def balanced_binary_tree(self, root):
        """judge balanced binary tree"""
        if not root:
            return True
        leftheight = self.get_height(root.left)
        rightheight = self.get_height(root.right)
        if abs(leftheight - rightheight) > 1:
            return False
        return self.balanced_binary_tree(root.left) and self.balanced_binary_tree(root.right)


    def update_height(self, node):
        """ Update the height of all nodes under the current node"""

        node.left_height = 0
        node.right_height = 0
        # Whether to the bottom of the
        if node.left == None and node.right == None:
            return
        else:
            if node.left:
                self.update_height(node.left)
                # The height of the current node is equal to the larger value of the height of the left
                # and right child nodes + 1
                node.left_height = max(node.left.left_height, node.left.right_height) + 1
            if node.right:
                self.update_height(node.right)
                # The height of the current node is equal to the larger value of the height of the left and
                # right child nodes + 1
                node.right_height = max(node.right.left_height, node.right.right_height) + 1
            # Check if there is still imbalance
            if node.left_height - node.right_height >= 2:
                self.left_avertence(node)
            elif node.left_height - node.right_height <= -2:
                self.right_avertence(node)

    def right_avertence(self, node):
        """right avertence"""
        # Right-handed, the father of the current node is the father.
        new_code = Node()
        new_code.data = node.data
        new_code.left = node.left
        best_left = self.best_left_right(node.right)
        v = node.data

        if best_left == node.right and best_left.left == None:
            # Indicate that the current node does not have a node.
            node.data = best_left.data
            node.right = best_left.right
        else:
            node.data = best_left.left.data
            best_left.left = best_left.left.right
        node.left = new_code
        self.update_height(node)


    def left_avertence(self, node):
        """left avertence"""
        new_code = Node()
        new_code.data = node.data
        new_code.right = node.right
        best_right = self.best_left_right(node.left, 1)
        v = node.data

        if best_right == node.left and best_right.right == None:
            # Indicate that the current node does not have a node.
            node.data = best_right.data
            node.left = best_right.left
        else:
            node.data = best_right.right.data
            best_right.right = best_right.right.left
        node.right = new_code
        self.update_height(node)

    # 返回node节点最左（右）子孙的父级
    def best_left_right(self, node, type=0):
        # type=0 默认找最左子孙
        if type == 0:
            if node.left == None:
                return node
            elif node.left.left == None:
                return node
            else:
                return self.best_left_right(node.left, type)
        else:
            if node.right == None:
                return node
            elif node.right.right == None:
                return node
            else:
                return self.best_left_right(node.right, type)

    # 前序(先中再左最后右)
    def front(self, node=None):
        if node == None:
            self.front_list = []
            node = self.root
        # 输出当前节点
        self.front_list.append(node.data)
        # 先判断左枝
        if not node.left == None:
            self.front(node.left)
        # 再判断右枝
        if not node.right == None:
            self.front(node.right)
        # 返回最终结果
        return self.front_list

    # 中序(先左再中最后右)
    def middle(self, node=None):
        if node == None:
            node = self.root
        # 先判断左枝
        if not node.left == None:
            self.middle(node.left)
        # 输出当前节点
        self.middle_list.append(node.data)
        # 再判断右枝
        if not node.right == None:
            self.middle(node.right)
        return self.middle_list

    # 后序(先左再右最后中)
    def after(self, node=None):
        if node == None:
            node = self.root
        # 先判断左枝
        if not node.left == None:
            self.after(node.left)
        # 再判断右枝
        if not node.right == None:
            self.after(node.right)
        self.after_list.append(node.data)
        return self.after_list

    # 节点删除
    def del_node(self, v, node=None):
        if node == None:
            node = self.root
            # 删除根节点
            if node.data == v:
                self.del_root(self.root)
                return
        # 删除当前节点的左节点
        if node.left:
            if node.left.data == v:
                self.del_left(node)
                return
        # 删除当前节点的右节点
        if node.right:
            if node.right.data == v:
                self.del_right(node)
                return
        if v > node.data:
            if node.right:
                self.del_node(v, node.right)
            else:
                print("删除的元素不存在")
        else:
            if node.left:
                self.del_node(v, node.left)
            else:
                print("删除的元素不存在")

    # 删除当前节点的右节点
    def del_right(self, node):
        # 情况1 删除节点没有右枝
        if node.right.right == None:
            node.right = node.right.left
        else:
            best_left = self.best_left_right(node.right.right)
            # 表示右枝最左孙就是右枝本身
            if best_left == node.right.right and best_left.left == None:
                node.right.data = best_left.data
                node.right.right = best_left.right
            else:
                node.right.data = best_left.left.data
                best_left.left = best_left.left.right

    # 删除当前节点的左节点
    def del_left(self, node):
        # 情况1 删除节点没有右枝
        if node.left.right == None:
            node.left = node.left.left
        else:
            best_left = self.best_left_right(node.left.right)
            # 表示右枝最左子孙就是右枝本身
            if best_left == node.left.right and best_left.left == None:
                node.left.data = best_left.data
                node.left.right = best_left.right
            else:
                node.left.data = best_left.left.data
                best_left.left = best_left.left.right

    # 删除根节点
    def del_root(self, node):
        if node.right == None:
            if node.left == None:
                node.data = None
            else:
                self.root = node.left
        else:
            best_left = self.best_left_right(node.right)
            # 表示右枝最左子孙就是右枝本身
            if best_left == node.right and best_left.left == None:
                node.data = best_left.data
                node.right = best_left.right
            else:
                node.data = best_left.left.data
                best_left.left = best_left.left.right

    # 搜索
    def search(self, v, node):
        if node == None:
            node = self.root
        if node.data == v:
            return True
        if v > node.data:
            if not node.right == None:
                return self.search(v, node.right)
        else:
            if not node.left == None:
                return self.search(v, node.left)
        return False


if __name__ == '__main__':
    # 需要建立二叉树的列表
    list = [4, 6, 3, 1, 7, 9, 8, 5, 2]
    t = BalancedBinaryTree()
    t.create_tree(0, list)
    res = t.front()
    print('前序', res)
    print(t.search(4, t.root))
    t.del_root(t.root)
    res = t.front()
    print('前序', res)

