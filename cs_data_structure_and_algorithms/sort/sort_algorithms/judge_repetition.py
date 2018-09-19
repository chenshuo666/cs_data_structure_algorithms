#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class JudgeRepetition(object):
    def __init__(self,array = []):
        self.get_array = []
        self.array = array
        
    def judge(self):
        for i in range(len(self.array)):
            for j in range(i+1,len(self.array)):
                if self.array[i] == self.array[j]:
                    self.get_array.append(self.array[i])
                    return True
        return False

if __name__=="__main__":
    mm = [3,2,5,7,23,6,8,5,3,6,9,89,65,78,0,6,4,5,8,54,7,891,2,4,6,6,345]
    t=JudgeRepetition(mm)
    print(t.judge())