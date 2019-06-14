# -*- encoding:utf-8 -*-
"""
@作者：wuchengan
@文件名：test_hikcommunity.py
@时间：2019/5/22  17:24
@文档说明:
"""


import unittest
from page.hikCommunity import *
from page.init import *

import time

class HikCommunityTest(Init,HikCommunity):
    
    def test_login_null_password(self):
        """登录业务：密码为空"""
        time.sleep(2)
        self.login(self.getExcelData('data.xlsx')[0][0],self.getExcelData('data.xlsx')[0][1])
        time.sleep(1)
        try:
            self.assertEqual(self.getLoginError, self.getExcelData('data.xlsx')[0][2])
            self.modifyExcel('data.xlsx', 2, 4, 'P',reason='')
        except Exception as e:
            self.modifyExcel('data.xlsx', 2, 4, 'F',repr(e))
        
    def test_login_null_username(self):
        """登录业务：用户名为空"""
        time.sleep(2)
        self.login(self.getExcelData('data.xlsx')[1][0],self.getExcelData('data.xlsx')[1][1])
        time.sleep(1)
        try:
            self.assertEqual(self.getLoginError,self.getExcelData('data.xlsx')[1][2])
            self.modifyExcel('data.xlsx', 3, 4, 'P',reason='')
        except Exception as e:
            self.modifyExcel('data.xlsx', 3, 4, 'F',repr(e))
        
    def test_login_success(self):
        """登录业务：登录成功"""
        time.sleep(2)
        self.login(self.getExcelData('data.xlsx')[2][0],self.getExcelData('data.xlsx')[2][1])
        time.sleep(1)
        try:
            self.assertEqual(self.getLoginSuccess,self.getExcelData('data.xlsx')[2][2])
            self.modifyExcel('data.xlsx', 4, 4, 'P',reason='')
        except Exception as e:
            self.modifyExcel('data.xlsx', 4, 4, 'F',repr(e))
        
if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite=unittest.TestSuite()
    suite.addTest(HikCommunityTest('test_login_null_password'))
    suite.addTest(HikCommunityTest('test_login_null_username'))
    suite.addTest(HikCommunityTest('test_login_success'))
    runner=unittest.TextTestRunner()
    runner.run(suite)