#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import sys

graphMatrix =  [[0, 2, 1, 4, 5, 1],
            [1, 0, 4, 2, 3, 4],
            [2, 1, 0, 1, 2, 4],
            [3, 5, 2, 0, 3, 3],
            [2, 4, 3, 4, 0, 1],
            [3, 4, 7, 3, 1, 0]]

treeDis = graphMatrix[0]  # 各个点距离生成树的最短距离列表
visited = [0 for i in range(6)]  # 已经访问过的节点将被置为1
visited[0] = 1
# 不在树中的点距离树有最短距离，在树中对应的距离最小的那个店
# 比如neighbor[1]=0表示在节点1还不在树中时，它离树中的节点0距离最小
neighbor = [0] * 6
for i in range(5):
    minDis = sys.maxsize
    minDisPos = int()
    print(minDis)
    # 找出此时离树距离最小的不在树中顶点
    for j in range(6):
        if (not visited[j]) and (treeDis[j] < minDis):
            minDis = treeDis[j]
            minDisPos = j

    visited[minDisPos] = 1
    print(minDisPos, minDis)
    # print("Here tree")
    # print(treeDis)
    for j in range(6):
        # 刷新剩下的顶点距离树的最短距离
        if (not visited[j]) and (graphMatrix[j][minDisPos] < treeDis[j]):
            treeDis[j] = graphMatrix[j][minDisPos]
            neighbor[j] = minDisPos
        # print("Here minDIsPos : "+str(minDisPos))

print(neighbor)
print("Edges that in the tree:")
for i in range(1, 6):
    print(str(i) + '-' + str(neighbor[i]))