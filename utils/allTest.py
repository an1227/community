# -*- encoding:utf-8 -*-
"""
@作者：wuchengan
@文件名：allTest.py
@时间：2019/5/23  17:59
@文档说明:
"""


import os
import time
import unittest
import HTMLTestRunner

def allTests():
    """获取所有需要执行的用例"""
    suite=unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'testCase'),\
        pattern='test_*.py')
    return suite
def getNowTime():
    """获取当前的时间"""
    now = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
    return now
def run():
    filename=os.path.dirname(os.path.dirname(__file__))+'\\report'+'\\'+getNowTime()+'UIreport.html'
    print(filename)
    fb=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title='UI自动化测试报告',
        verbosity=2,
        description='详细的UI自动化测试报告'
    )
    runner.run(allTests())
    
if __name__ == '__main__':
    run()