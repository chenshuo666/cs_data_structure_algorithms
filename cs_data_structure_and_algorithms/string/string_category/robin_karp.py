#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams


class RabinKarp(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.hash_str1 = 0
        self.hash_str2 = 0

        self.init = 0
        self.end = len(self.str2)
    
    def set_hash_str1(self, str1, size):
        for i in range(0, size):
            self.hash_str1 += ord(str1[i])#hash采用ASC值

    def set_hash_str2(self, str2, size):
        for i in range(0, size):
            self.hash_str2 += ord(str2[i])

    def move(self): #前移一个单位
        if self.end <= len(self.str1) - 1:
            self.hash_str1 -= ord(self.str1[self.init])
            self.hash_str1 += ord(self.str1[self.end])
            self.init += 1
            self.end += 1

    def get_hash_str1_value(self):
        return self.hash_str1

    def get_hash_str2_value(self):
        return self.hash_str2

    def text(self):
        return self.str1[self.init:self.end]


    def rabin_karp(self):
        list_index = []
        if self.str2 == None or self.str1 == None:
            return -1
        if self.str2 == "" or self.str1 == "":
            return -1
    
        if len(self.str2) > len(self.str1):
            return -1

        self.set_hash_str1(self.str1, len(self.str2))
        self.set_hash_str2(self.str2, len(self.str2))
    
        for i in range(len(self.str1) - len(self.str2) + 1):
            if self.get_hash_str1_value() == self.get_hash_str2_value():
                if self.text() == self.str2:
                    list_index.append(i)
            self.move()
    
        return list_index


if __name__ == "__main__":
    t = RabinKarp("adbcbdc", "dc")
    print(t.rabin_karp())