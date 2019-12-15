#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time    : 2019-12-10 10:37
#@Author  : hcj
import unittest
class test (unittest.TestCase):
    print(" this is class Test")
    def setup(self):
        print("this is setp")
    def test_1(self):
        print("this is testcase 1")
    def tearDown(self):
        print("this is tearDown")
if __name__ == '__main__':

    unittest.main()
    print ("this is __name__")