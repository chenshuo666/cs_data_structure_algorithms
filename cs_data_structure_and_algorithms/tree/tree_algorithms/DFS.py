#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

# *args 把参数打包成tuple供函数调用。**kwargs把 x = a，y=b打包成字典{x:a,y:b}供函数调用
class Graph(object):
    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if (u != v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    # 递归DFS
    def depth_first_search(self, root=None):
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)

        if root:
            dfs(root)

        # 对于不连通的结点（即dfs（root）完仍是没有visit过的单独处理，再做一次dfs
        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        self.visited = {}
        print(order)
        return order

    # 非递归DFS
    def depth_first_search2(self, root=None):
        stack = []
        order = []

        # self.visited[root] = True
        def dfs():
            while stack:
                node = stack[-1]
                for n in self.node_neighbors[node]:
                    if not n in self.visited:
                        order.append(n)
                        stack.append(n)
                        self.visited[n] = True
                        break
                else:
                    stack.pop()

        if root:
            stack.append(root)
            order.append(root)
            self.visited[root] = True
            dfs()

        for node in self.nodes():
            if node not in self.visited:
                stack.append(node)
                order.append(node)
                self.visited[node] = True
                dfs()

        self.visited = {}
        print(order)
        return order

    def breadth_first_search(self, root=None):
        queue = []
        order = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()

        self.visited = {}
        print(order)
        return order


if __name__ == '__main__':
    g = Graph()
    g.add_nodes([i + 1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print("nodes:", g.nodes())

    print("BFS：")
    order = g.breadth_first_search(1)
    # self.visited 在经历了一次bfs之后已经有了值，如果dfs直接进行，就会发生只输出结点1的情况
    print("递归DFS：")
    print(g.depth_first_search(1))
    print("非递归DFS")
    print(g.depth_first_search2(1))
