# -*- encoding:utf-8 -*-
"""
@作者：wuchengan
@文件名：init.py
@时间：2019/5/23  17:51
@文档说明:
"""


import unittest
from selenium import webdriver
from utils.operationXlsx import *

class Init(unittest.TestCase,OperationExcel):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('https://sq.hik-cloud.com')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

