#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-16 14:02
#@Author  : hcj
list1=['中国','美国',1997,2000]
print(list1.remove(1997))
print(list1.pop(2))
print(list1.pop())
print(list1)
list1.append(2003)
list1.append(2008)
list1.append(2009)
print(list1)
L=[]
for x in range(1,10):
    L.append(x*x)
print(L)
d={"x":"a","y":"b","z":"c"}
for k,v in d.items():
    print(k)
    print(v)
tup1=("中国","美国",1997,2000)
tup2=("1,2,3,4,5")
tup3="a","b","c","d"
