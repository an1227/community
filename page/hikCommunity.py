# -*- encoding:utf-8 -*-
"""
@作者：wuchengan
@文件名：hikCommunity.py
@时间：2019/5/22  17:04
@文档说明:
"""

from base.basePage import *
from selenium.webdriver.common.by import By

class HikCommunity(WebDriver):
    username_loc=(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[1]/form/div[1]/input')
    password_loc=(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[1]/form/div[2]/input')
    login_loc=(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[1]/form/div[4]/div/button')
    loginError_loc=(By.XPATH,'/html/body/div[2]/div[2]/p')
    loginSuccess_loc=(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div[3]/div/div[2]')
    
    def typeUserName(self,username):
        self.findElement(*self.username_loc).clear()
        self.findElement(*self.username_loc).send_keys(username)
        
    def typePassword(self,password):
        self.findElement(*self.password_loc).clear()
        self.findElement(*self.password_loc).send_keys(password)
        
    
    def clickLogin(self):
        self.findElement(*self.login_loc).click()
    
    def login(self,username,password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin()
        
    @property
    def getLoginError(self):
        """获取错误的信息"""
        return self.findElement(*self.loginError_loc).text
    @property
    def getLoginSuccess(self):
        """获取登录成功信息"""
        return self.findElement(*self.loginSuccess_loc).text


