#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams
import networkx as nx
import matplotlib.pyplot as plt

class DisjointSet(dict):
    '''不相交集'''

    def __init__(self, dict):
        pass

    def add(self, item):
        self[item] = item

    def find(self, item):
        if self[item] != item:
            self[item] = self.find(self[item])
        return self[item]

    def unionset(self, item1, item2):
        self[item2] = self[item1]


def Kruskal_1(nodes, edges):
    '''基于不相交集实现Kruskal算法'''
    forest = DisjointSet(nodes)
    MST = []
    for item in nodes:
        print(item)
        forest.add(item)
    edges = sorted(edges, key=lambda element: element[2])
    num_sides = len(nodes) - 1  # 最小生成树的边数等于顶点数减一
    for e in edges:
        node1, node2, _ = e
        parent1 = forest.find(node1)
        parent2 = forest.find(node2)
        if parent1 != parent2:
            MST.append(e)
            num_sides -= 1
            if num_sides == 0:
                return MST
            else:
                forest.unionset(parent1, parent2)
    pass

def main():
    nodes = ['A','B','C','D','E','F','G','H','I']
    edges = [("A", "B", 4), ("A", "H", 8),
             ("B", "C", 8), ("B", "H", 11),
             ("C", "D", 7), ("C", "F", 4),
             ("C", "I", 2), ("D", "E", 9),
             ("D", "F", 14), ("E", "F", 10),
             ("F", "G", 2), ("G", "H", 1),
             ("G", "I", 6), ("H", "I", 7)]
    print("The minimum spanning tree by Kruskal is : ")
    print(Kruskal_1(nodes, edges))

    G = nx.Graph()  # 建立一个空的无向图G
    for node in nodes:
        G.add_node(str(node))
    for edge in Kruskal_1(nodes, edges):
        G.add_edge(str(edge[0]), str(edge[1]))

    # print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
    # print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
    # print("number of edges:", G.number_of_edges())  # 输出边的数量：1
    nx.draw(G, with_labels=True)
    plt.savefig('fig.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()