#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

class FiniteAutomaton(object):
    def __init__(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        self.num_char = 256

    def getNextState(self,pat,M,state,x):
        if state<M and x == pat[state]:
            return state+1
        ns = state
        while ns > 0:
            if pat[ns-1] == x:
                i=0
                while i<ns-1:
                    if pat[i] != pat[state-ns+1+i]:
                        break
                    i+=1
                if i==ns-1:
                    return ns
            ns-=1
        return 0

    def compute_transition_function(self,pat,M,TF):
        state , x = 0 , 0
        while state <= M:
            while x < self.num_char:
                TF[state].append(self.getNextState(pat,M,state,x))
                x+=1
            state +=1

    def finite_automata_search(self):
        M = len(self.arr1)
        N = len(self.arr2)

        TF_len = M+1
        TF = [([ ] * TF_len) for i in range(self.num_char)]
        self.compute_transition_function(self.arr1, M, TF)
        state = 0
        for i in range(N):
            state = TF[state][i]
            if (state == M):
                print("patterb found at index is: {}".format(i-M+1))


if __name__ =="__main__":
    txt = "Finite Automata Algorithm: Finite Automata"
    pat = "Auto"
    t=FiniteAutomaton(pat,txt)
    t.finite_automata_search()

