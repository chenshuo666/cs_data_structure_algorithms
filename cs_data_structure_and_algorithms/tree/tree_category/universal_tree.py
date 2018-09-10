#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def getdata(self):
        return self.data

    def getchildren(self):
        return self.children

    def add(self, node):
        ##if full
        if len(self.children) == 4:
            return False
        else:
            self.children.append(node)

    def go(self, data):
        for child in self.children:
            if child.getdata() == data:
                return child
        return None


class tree:
    def __init__(self):
        self._head = node('header')

    def linktohead(self, node):
        self._head.add(node)

    def insert(self, path, data):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return False
            else:
                cur = cur.go(step)
        cur.add(node(data))
        return True

    def search(self, path):
        cur = self._head
        for step in path:
            if cur.go(step) == None:
                return None
            else:
                cur = cur.go(step)
        return cur

if __name__=="__main__":

    '''
    define node
    '''
    a = node('A')
    b = node('B')
    c = node('C')
    d = node('D')
    e = node('E')
    f = node('F')
    g = node('G')
    h = node('H')
    i = node('I')
    j = node('J')
    k = node('K')
    l = node('L')
    m = node('M')
    n = node('N')
    o = node('O')

    '''
    adding node to build true
    '''
    a.add(b)
    a.add(g)
    a.add(h)
    b.add(c)
    b.add(e)
    g.add(i)
    g.add(j)
    g.add(k)
    g.add(l)
    h.add(m)
    h.add(n)
    h.add(o)
    c.add(d)
    c.add(f)
    i.add(node(29))
    j.add(node(28))
    k.add(node(27))
    l.add(node(26))
    m.add(node(25))
    n.add(node(24))
    o.add(node(23))
    f.add(node(30))

    tree = tree()
    tree.linktohead(a)

    # testcase
    print('Node', tree.search("ABE").getdata())
    print('Node', tree.search("ABC").getdata())
    print('Node', tree.search("AHM").getdata())
    tree.insert("ABCD", 1)
    for i in d.getchildren():
        print('value after', d.getdata(), ' is ', i.getdata())