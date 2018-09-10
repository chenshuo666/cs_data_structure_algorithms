#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

map = []

for i in range(0, 10):
  map += [[]]
  for j in range(0, 20):
    map[i] += ['*']

print(map[0][1])
map[0][1] = 10
print(map[0][1])





