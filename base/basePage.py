# -*- encoding:utf-8 -*-
"""
@作者：wuchengan
@文件名：basePage.py
@时间：2019/5/22  17:03
@文档说明:
"""

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver
    
    def findElement(self, *loc):
        """单个元素定位方法"""
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('Error Detail{0}'.format(e.args[0]))
    
    def findElements(self, *loc):
        """多个元素定位方法"""
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print('Error Detail{0}'.format(e.args[0]))

