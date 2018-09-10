#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

class SplayTree(object):
    class __SplayNode(object):
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            if (self.key != None):
                yield self.key

            if self.right != None:
                for elem in self.right:
                    yield elem

        # 迭代的是Node类型，用于删除结点
        def iternodes(self):
            if self.left != None:
                for elem in self.left.iternodes():
                    yield elem

            if self != None and self.key != None:
                yield self

            if self.right != None:
                for elem in self.right.iternodes():
                    yield elem

        def info(self):
            s = 'Key=' + str(self.key) + ', ' + \
                'LChild=' + str(self.left) + ', ' + \
                'RChild=' + str(self.right)
            print(s)

        def __str__(self):
            return str(self.key)

        def __repr__(self):
            if self != None:
                s_1 = str(self.key)
            else:
                s_1 = 'None'

            if self.left != None:
                s_2 = str(self.left.key)
            else:
                s_2 = 'None'

            if self.right != None:
                s_3 = str(self.right.key)
            else:
                s_3 = 'None'

            return '__SplayNode(' + s_1 + ', ' + s_2 + ', ' + s_3 + ')'

    def __init__(self):
        self.root = None
        self.header = SplayTree.__SplayNode(None)  # For splay()

    # LL
    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        return k1

    # RR
    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        return k1

    # RL
    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    # LR
    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    # 伸展运动
    def splay(self, key):
        l = r = self.header
        t = self.root
        if t is None:
            return

        self.header.left = self.header.right = None

        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    t = self.singleLeftRotate(t)
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left

            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    t = self.singleRightRotate(t)
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break

        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t

    #
    # 和splay操作捆绑的方法
    #

    # 插入
    def insert(self, key):
        if (self.root == None):
            self.root = SplayTree.__SplayNode(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = SplayTree.__SplayNode(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if self.root is None or key != self.root.key:
            return None

        # Now delete the root.
        if self.root.left == None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

        return key;

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None

    #
    # 结构信息查询，不与splay操作捆绑
    #

    def getRoot(self):
        return repr(self.root)

    def info(self):
        a = []
        for x in self:
            a.append(x)

        print(a)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def __contains__(self, val):
        for x in self:
            if (x == val):
                return True

        return False

    def __len__(self):
        a = []
        for x in self:
            a.append(x)
        return len(a)

    # 求结点高度
    def height(self, node):
        if (node == None):
            return 0
        else:
            m = self.height(node.left)
            n = self.height(node.right)
            return max(m, n) + 1

        # 传回结点的原始信息

    def iternodes(self):
        if self.root != None:
            return self.root.iternodes()
        else:
            return [None]

    # 寻找节点路径
    def findNodePath(self, root, node):
        path = []
        if root == None or root.key == None:
            path = []
            return path

        while (root != node):
            if node.key < root.key:
                path.append(root)
                root = root.left
            elif node.key >= root.key:
                path.append(root)
                root = root.right
            else:
                break

        path.append(root)
        return path

    # 寻找父结点
    def parent(self, root, node):
        path = self.findNodePath(root, node)
        if (len(path) > 1):
            return path[-2]
        else:
            return None

    # 是否左孩子
    def isLChild(self, parent, lChild):
        if (parent.getLeft() != None and parent.getLeft() == lChild):
            return True

        return False

    # 是否右孩子
    def isRChild(self, parent, rChild):
        if (parent.getRight() != None and parent.getRight() == rChild):
            return True

        return False

    # 求某元素是在树的第几层
    # 约定根为0层
    # 这个计算和求结点的Height是不一样的
    def level(self, elem):
        if self.root != None:
            node = self.root
            lev = 0

            while (node != None):
                if elem < node.key:
                    node = node.left
                    lev += 1
                elif elem > node.key:
                    node = node.right
                    lev += 1
                else:
                    return lev

            return -1

        else:
            return -1


if __name__ == '__main__':
    splay = SplayTree()

    a = [20, 30, 40, 120, 13, 39, 38, 40, 18, 101]

    for item in a:
        splay.insert(item)
        print(splay.getRoot())
        print(splay.height(splay.root))

    splay.info()
    print(len(splay))

    for node in splay.iternodes():
        print(splay.findNodePath(splay.root, node), '\n')

    '''
    for item in reversed(a):
        print('remove:', splay.remove(item));
        splay.getRoot();
        print(splay.height(splay.root));
    '''

    print(splay.findMax())
    print(splay.getRoot())
