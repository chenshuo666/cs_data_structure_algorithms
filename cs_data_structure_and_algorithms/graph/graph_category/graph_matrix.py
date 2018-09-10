#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

# 图的节点结构
import networkx as nx
import matplotlib.pyplot as plt

class GraphMatrix:
    def __init__(self, vertice=[], matrix=[] ):
        self.matrix = matrix  # 图的矩阵结构
        self.vertice = vertice # 顶点的表示

        self.edges_dict = {}  # {(tail, head):weight}有权图
        self.edges_array = []  # (tail, head, weight)
        self.edges_array_copy = []

        self.edge_num = 0
        self.vertice_num = len(vertice)

        if len(matrix) > 0:
            if len(vertice) != len(matrix):
                raise IndexError
            self.edges = self.get_all_edges()

        # if do not provide a adjacency matrix, but provide the vertice list, build a matrix with 0
        elif len(vertice) > 0:
            self.matrix = [[0 for col in range(len(vertice))] for row in range(len(vertice))]

    def isOutRange(self, x):
        try:
            if x >= self.vertice_num or x <= 0:
                raise IndexError
        except IndexError:
            print("OUT RANGE")

    '''顶点的操作'''
    def get_all_vertice(self):#获取所有的顶点
        return self.vertice

    def get_vertice_num(self):#获取顶点的数目
        self.vertice_num = len(self.matrix)
        return self.vertice_num

    def add_vertice(self,vertice,matrix_in):#增加一个顶点
        if vertice not in self.vertice:
            self.vertice.append(vertice)
        for i in range(self.vertice_num):
            self.matrix[i].append(0)
        self.vertice_num = self.vertice_num + 1
        if matrix_in[-1] == 0 and self.vertice_num == len(matrix_in):
            self.matrix.append(matrix_in)
        else:
            return

    def delete_vertice(self, x):#删除一个顶点
        index_t = 0
        if x in self.vertice:
            for i in range(len(self.vertice)):
                if x==self.vertice[i]:
                    index_t=i
            for i in range(self.vertice_num):
                if self.matrix[i][index_t] is 1:
                    self.matrix[i][index_t] = 0
                    self.edge_num = self.edge_num - 1
                if self.matrix[index_t][i] is 1:
                    self.matrix[index_t][i] = 0
                    self.edge_num = self.edge_num - 1
            self.vertice.remove(x)
            list(map(lambda delete: delete[index_t:], self.matrix))
            self.matrix.remove(self.matrix[index_t])


    '''边的操作'''
    def get_all_edges(self):#获取所有的边
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if  self.matrix[i][j] != 0:
                    self.edges_dict[self.vertice[i], self.vertice[j]] = self.matrix[i][j]
                    self.edges_array.append([self.vertice[i], self.vertice[j], self.matrix[i][j]])

        return self.edges_array

    def get_edge_num(self):#获取边的数目
        self.edge_num = 0
        for i in range(self.vertice_num):
            for j in range(self.vertice_num):
                if self.matrix[i][j] is 1:
                    self.edge_num = self.edge_num + 1
        return self.edge_num

    def add_edge(self, vertice1, vertice2):#增加一条边
        index1 = 0
        index2 = 0
        if vertice1 in self.vertice and vertice2 in self.vertice:
            for i in range(len(self.vertice)):
                if vertice1 == self.vertice[i]:
                    index1 = i
            for t in range(len(self.vertice)):
                if vertice2 == self.vertice[t]:
                    index2 = t

            if self.matrix[index1][index2] is 0:
                self.matrix[index1][index2] = 1
                self.edge_num = self.edge_num + 1

    def remove_edge(self, vertice1, vertice2):#删除边
        index1 = 0
        index2 = 0
        if vertice1 in self.vertice and vertice2 in self.vertice:
            for i in range(len(self.vertice)):
                if vertice1 == self.vertice[i]:
                    index1 = i
            for t in range(len(self.vertice)):
                if vertice2 == self.vertice[t]:
                    index2 = t
            if self.matrix[index1][index2] is 1:
                self.matrix[index1][index2] = 0
                self.edge_num = self.edge_num - 1
            else:
                return
        else:
            return

    '''图的遍历'''

    def dfs(self,x):
        index_t = 0
        if x in self.vertice:
            for i in range(len(self.vertice)):
                if x == self.vertice[i]:
                    index_t = i
        res = []
        visited = [False]*self.vertice_num
        def DFS(i):
            res.append(self.vertice[i])
            visited[i] = True
            for j in range(self.vertice_num):
                if self.matrix[i][j] > 0 and visited[j] == False:
                    DFS(j)
        if self.vertice_num > 0:
            DFS(index_t)
        for i in range(self.vertice_num):
            if visited[i] == False:
                DFS(i)
        return res

    def bfs(self,x):
        index_t = 0
        if x in self.vertice:
            for i in range(len(self.vertice)):
                if x == self.vertice[i]:
                    index_t = i
        queue = []
        visited = [False] * self.vertice_num
        res = []

        def BFS():
            while len(queue) > 0:
                i = queue.pop(0)
                for j in range(self.vertice_num):
                    if self.matrix[i][j] > 0 and visited[j] == False:
                        res.append(self.vertice[j])
                        visited[j] = True
                        queue.append(j)

        if self.vertice_num <= 0:
            return res
        else:
            queue.append(index_t)  # index, value
            visited[0] = True
            res.append(self.vertice[index_t])
            BFS()

        for i in range(self.vertice_num):
            if visited[i] == False:
                res.append(self.vertice[i])
                visited[i] = True
                queue.append(i)
                BFS()
        return res

    def floyd(self, vertice, matrix):
        length = len(matrix)
        path = {}
        for i in range(length):
            path.setdefault(i, {})
            for j in range(length):
                if i == j:
                    continue
                path[i].setdefault(j, [i,j])
                node = None

                for k in range(length):
                    if k == j:
                        continue
                    dis = matrix[i][k] + matrix[k][j]
                    if matrix[i][j] > dis:
                        matrix[i][j] = dis
                        node = k
                if node:
                    path[i][j].insert(-1, node)
        return matrix, path

    def dijkstra(self, vertice_in, matrix, src):
        # 判断图是否为空，如果为空直接退出
        list_road  = []
        if matrix is None:
            return None
        vertice = [i for i in range(len(matrix))]  # 获取图中所有节点
        visited = []  # 表示已经路由到最短路径的节点集合
        if src in vertice:
            visited.append(src)
            vertice.remove(src)
        else:
            return None
        distance = {src: 0}  # 记录源节点到各个节点的距离
        for i in vertice:
            distance[i] = matrix[src][i]  # 初始化
        # print(distance)
        path = {src: {src: []}}  # 记录源节点到每个节点的路径
        k = pre = src
        while vertice:
            mid_distance = float('inf')
            for v in visited:
                for d in vertice:
                    new_distance = matrix[src][v] + matrix[v][d]
                    if new_distance < mid_distance:
                        mid_distance = new_distance
                        matrix[src][d] = new_distance  # 进行距离更新
                        k = d
                        pre = v
            distance[k] = mid_distance  # 最短路径
            path[src][k] = [i for i in path[src][pre]]
            path[src][k].append(k)
            # 更新两个节点集合
            visited.append(k)
            vertice.remove(k)
            print(visited, vertice)  # 输出节点的添加过程

        return distance, path

    def create_matrix(self):
        graph_by_anthor = GraphMatrix(self.vertice, self.matrix)
        print(graph_by_anthor)
        return graph_by_anthor

    def draw_undirected_graph(self,graph_by_anthor): #无向无权图可视化
        G = nx.Graph()  # 建立一个空的无向图G
        for node in graph_by_anthor.vertice:
            G.add_node(str(node))
        for edge in graph_by_anthor.edges_array:
            G.add_edge(str(edge[0]), str(edge[1]))

        # print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
        # print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
        # print("number of edges:", G.number_of_edges())  # 输出边的数量：1
        nx.draw(G, with_labels=True)
        plt.savefig('fig.png', bbox_inches='tight')
        plt.show()

    def draw_directed_graph(self,graph_by_anthor):
        G = nx.DiGraph()  # 建立一个空的有向图G
        for node in graph_by_anthor.vertice:
            G.add_node(str(node))
        G.add_weighted_edges_from(graph_by_anthor.edges_array)

        # print("nodes:", G.nodes())  # 输出全部的节点
        # print("edges:", G.edges())  # 输出全部的边
        # print("number of edges:", G.number_of_edges())  # 输出边的数量
        nx.draw(G, with_labels=True)
        plt.savefig("directed_graph.png", bbox_inches='tight')
        plt.show()

if __name__ == "__main__":

    nodes = ['0', '1', '2', '3', '4', '5']
    matrix = [[0, 2, 1, 4, 5, 1],
            [1, 0, 4, 2, 3, 4],
            [2, 1, 0, 1, 2, 4],
            [3, 5, 2, 0, 3, 3],
            [2, 4, 3, 4, 0, 1],
            [3, 4, 7, 3, 1, 0]]
    # matrix_in = [0 ,0,0,0,0,0,0,1,0]
    m=GraphMatrix(nodes,matrix)
    # m.add_vertice("i",matrix_in)
    # # m.add_edge(6,4)
    # print(m.get_all_edges())
    # print(m.get_all_vertice())
    # print("__________________")
    # print(m.get_edge_num())
    # print(m.get_vertice_num())
    # print(m.dfs("c"))
    # print(m.bfs("a"))
    # # m.delete_vertice("i")
    #
    # new_graph, path= m.dijkstra(matrix,1)
    # print(new_graph,path)

    p=m.create_matrix()
    m.draw_directed_graph(p)

