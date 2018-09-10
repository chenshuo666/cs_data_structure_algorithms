#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

# 图的节点结构
class DirectedNode:
    def __init__(self, value):
        self.value = value      # 节点值
        self.come = 0           # 节点入度
        self.out = 0            # 节点出度
        self.nexts = []         # 节点的邻居节点
        self.edges = []         # 在节点为from的情况下，边的集合

class DirectedEdge:
    def __init__(self, weight, from_node, to_node):
        self.weight = weight        # 边的权重
        self.from_node = from_node              # 边的from节点
        self.to_node = to_node                # 边的to_node节点

class Graph:
    def __init__(self):
        self.nodes = {}     # 图的所有节点集合  字典形式：{节点编号：节点}
        self.edges = []     # 图的边集合
        self.node_num = 0
        self.edge_num = 0

    # 生成图结构
    # matrix = [
    #   [1,2,3],        ==>   里面分别代表权重, from节点, to_node节点
    #   [...]
    # ]
    def createGraph_matrix(self,matrix):
        for edge in matrix:
            weight = edge[0]
            from_node = edge[1]
            to_node = edge[2]
            if from_node not in self.nodes:
                self.nodes[from_node] = DirectedNode(from_node)
            elif to_node not in self.nodes:
                self.nodes[to_node] = DirectedNode(to_node)
            else:
                from_Node = self.nodes[from_node]
                to_Node = self.nodes[to_node]
                newEdge = DirectedEdge(weight, from_Node, to_Node)
                from_Node.nexts.append(to_Node)
                from_Node.out += 1
                to_Node.come += 1
                from_Node.edges.append(newEdge)
                self.edges.append(newEdge)

    def get_node_num(self):
        return len(self.nodes)

    def get_edge_num(self):
        return len(self.edges)

if __name__ == '__mian__':
    list_graph = [[12,3,4],[21,3,6],[23,1,3],[34,2,3],[45,3,5],[33,5,6],[23,5,2]]
    t = Graph()
    m = t.createGraph_matrix(list_graph)
    print(m.get_node_num())