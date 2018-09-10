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


# 二叉树对象
class BalancedBinaryTree(object):
    def __init__(self):
        self.root = None
        self.front_list = []
        self.middle_list = []
        self.after_list = []

    # 生成二叉树
    def create_tree(self, n=0, l=()):
        if l == []:
            print("传入的列表为空")
            return
        if n > len(l) - 1:
            print("二叉树生成")
            return
        node = Node()
        node.data = l[n]
        if not self.root:
            self.root = node
            self.list = l
        else:
            self.add(self.root, node)
        self.create_tree(n + 1, l)

    # 添加节点
    def add(self, parent, new_node):
        if new_node.data > parent.data:
            # 插入值比父亲值大，所以在父节点右边
            if parent.right == None:
                parent.right = new_node
                # 新插入节点的父亲节点的高度值为1，也就是子高度值0+1
                parent.right_height = 1
                # 插入值后 从下到上更新节点的height
            else:
                self.add(parent.right, new_node)
                # 父亲节点的右高度等于右孩子，左右高度中较大的值 + 1
                parent.right_height = max(parent.right.right_height, parent.right.left_height) + 1
                # ======= 此处开始判断平衡二叉树=======
                # 右边高度大于左边高度 属于右偏
                if parent.right_height - parent.left_height >= 2:
                    self.right_avertence(parent)
        else:
            # 插入值比父亲值小，所以在父节点左边
            if parent.left == None:
                parent.left = new_node
                parent.left_height = 1
            else:
                self.add(parent.left, new_node)
                parent.left_height = max(parent.left.right_height, parent.left.left_height) + 1
                # ======= 此处开始判断平衡二叉树=======
                # 左边高度大于右边高度 属于左偏
                if parent.left_height - parent.right_height >= 2:
                    self.left_avertence(parent)

    def get_height(self, root):
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
        if not root:
            return True
        leftheight = self.get_height(root.left)
        rightheight = self.get_height(root.right)
        if abs(leftheight - rightheight) > 1:
            return False
        return self.balanced_binary_tree(root.left) and self.balanced_binary_tree(root.right)

    # 更新当前节点下的所有节点的高度
    def update_height(self, node):
        # 初始化节点高度值为0
        node.left_height = 0
        node.right_height = 0
        # 是否到最底层的一个
        if node.left == None and node.right == None:
            return
        else:
            if node.left:
                self.update_height(node.left)
                # 当前节点的高度等于左右子节点高度的较大值 + 1
                node.left_height = max(node.left.left_height, node.left.right_height) + 1
            if node.right:
                self.update_height(node.right)
                # 当前节点的高度等于左右子节点高度的较大值 + 1
                node.right_height = max(node.right.left_height, node.right.right_height) + 1
            # 检查是否仍有不平衡
            if node.left_height - node.right_height >= 2:
                self.left_avertence(node)
            elif node.left_height - node.right_height <= -2:
                self.right_avertence(node)

    def right_avertence(self, node):
        # 右偏 就将当前节点的最左节点做父亲
        new_code = Node()
        new_code.data = node.data
        new_code.left = node.left
        best_left = self.best_left_right(node.right)
        v = node.data
        # 返回的对象本身,
        if best_left == node.right and best_left.left == None:
            # 说明当前节点没有有节点
            node.data = best_left.data
            node.right = best_left.right
        else:
            node.data = best_left.left.data
            best_left.left = best_left.left.right
        node.left = new_code
        self.update_height(node)

    # 处理左偏情况
    def left_avertence(self, node):
        new_code = Node()
        new_code.data = node.data
        new_code.right = node.right
        best_right = self.best_left_right(node.left, 1)
        v = node.data
        # 返回的对象本身,
        if best_right == node.left and best_right.right == None:
            # 说明当前节点没有有节点
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

