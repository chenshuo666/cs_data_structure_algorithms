#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import sys
class GraphAdjacency(object):
    def __init__(self,dict):
        self.graph = dict
        # {'1': ['3', '4'], '2': ['5', '4'], '3': ['6'], '4': ['3', '7', '6'], '5': ['7', '4'], '7': ['6']}

    def find_path(self,start,end,path=[]):
        path = path+[start]
        if start==end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node,end,path)
                if newpath:
                    return newpath
        return None

    def find_paths(self,start,end,path=[]):
        path = path+[start]
        if start==end:
            return [path]
        if start not in self.graph:
            return None
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_paths(node,end,path)
                if newpath:
                    paths=paths + newpath
        return paths

    def find_shortest_path(self,start,end,path=[]):
        path = path+[start]
        if start==end:
            return path
        if start not in self.graph:
            return None
        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(node,end,path)
                if newpath:
                    if not shortest or len(shortest)>len(newpath):
                        shortest = newpath
        return shortest

    def dfs(self):
        stack = []
        visited = set()
        for key in self.graph:
            if key not in visited:
                stack.append(key)
                visited.add(key)
            while len(stack)>0:
                tmp = stack[len(stack)-1]
                if tmp not in self.graph:
                    if len(stack)>0:
                        stack.pop()
                        continue
                for value in self.graph[tmp]:
                    if value not in visited:
                        sys.stdout.write(value+" ")
                        stack.append(value)
                        visited.add(value)
                    else:
                        if len(stack)>0:
                            stack.pop()
                            continue
    def bfs(self):
        from collections import deque
        queue = deque()
        visited=set()
        for key in self.graph.keys():
            if key not in visited:
                queue.append(key)
                visited.add(key)
            while len(queue)>0:
                tmp = queue.popleft()
                sys.stdout.write(tmp+'\t')
                if tmp not in self.graph:
                    break
                for value in self.graph[tmp]:
                    if value not in visited:
                        queue.append(value)
                        visited.add(value)

    def has_circle(self):
        from collections import deque
        visited = set()
        for key in self.graph.keys():
            if key not in visited:
                queue = deque(key)
                visited.add(key)
                while len(queue)>0:
                    tmp = queue.popleft()
                    if tmp not in self.graph:
                        for value in self.graph[tmp]:
                            if key==value:
                                print("There is circle")
                                return
                            if value not in visited:
                                visited.add(value)
                                queue.append(value)
        print("There is not circle")
        return

if __name__=="__main__":
    dict={ '1':['3','4'], '2':['5','4'], '3':['6'], '4':['3','7','6'], '5':['7','4'], '7':['6'] }
    s=GraphAdjacency(dict)
    sys.stdout.write("Breadth first search:"+'\n')
    s.bfs()
    sys.stdout.write('\n')
    sys.stdout.write("Depth first search:"+'\n')
    s.dfs()
    sys.stdout.write('\n')
    sys.stdout.write("search a path:" + '\n')
    print(s.find_path('1','6'))
    sys.stdout.write("search all paths:" + '\n')
    print(s.find_paths('1','6'))
    sys.stdout.write("search the shortest path:" + '\n')
    print(s.find_shortest_path('1','6'))
    sys.stdout.write("judge circle:" + '\n')
    s.has_circle()
