#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-10 19:30
#@Author  : hcj
# list=[1,16,9,10,8,20]
# # list.sort()
# # print(list)
# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)
#
# delimiter=','
# mylist=['lily','lucy','india','china']
# print(delimiter.join(mylist))
#
#

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%2d "%(i,j,i*j),end='')
#     print()
#
# import time
# for i in range(4):
#     print(str(int(time.time()))[-2:])
#     time.sleep(1)
# print(time.time())
#
#
# for i in range(4):
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#     time.sleep(1)
#
# for i in range(4):
#     print(time.strftime('%Y-%M-%d %H:%M:%S',time.localtime(time.time())))
#
#
#
#
#
#
# res=1
# for i in range(20,1,-1):
#     res=i*res+1
# print(res)
#
# a=['one','two','three']
# print(a[::-1])
# #
# L = [1,2,3,4,5]
#
# L = [1,2,3,4,5]
# # for n in L:
# print(','.join(str(n)for n in L))
#
# # print(','.join(str(n) for n in L))
#
#
# seq3 = ('hello','good','boy','doiido')
# print(seq3)
# print (':'.join(seq3),'\n')
#
#
# if __name__ == '__main__':
#     person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
#     m = 'li'
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key
#
#     print('%s,%d' % (m, person[m]))

import random
import string

a = [1,2,3,4,5]
#1
print(random.choices(a,k=3))

print (random.choice(['剪刀', '石头', '布']))
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print (ran_str)
print (random.sample('zyxwvutsrqponmlkjihgfedcba',5))