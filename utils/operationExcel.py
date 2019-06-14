# -*- encoding:utf-8 -*-
"""
@作者：wuchengan
@文件名：operationExcel.py
@时间：2019/5/22  18:22
@文档说明:
"""


import xlrd,os,xlwt
from xlutils.copy import copy

class OperationExcel(object):
    def dir_base(self,filename,filePath='data'):
        """
        获取data文件夹下的文件
        :param filename: 要读取的文件名称
        :param filePath: 要读取的文件对应的文件夹
        :return:
        """
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filePath,filename)
    
    def getExcelData(self,filename):
        """
        获取Excel数据
        :param filename:Excel文件名
        :return: rows
        """
        rows=[]
        with xlrd.open_workbook(self.dir_base(filename)) as f:
            sheet=f.sheet_by_index(0) #获取excel第一张sheet表
            for row_idx in range(1,sheet.nrows):
                rows.append(sheet.row_values(row_idx,0,sheet.ncols-1))
            return rows
        
    def modifyExcel(self,filename,row,col,result):
        """
        修改Excel内容--->添加测试执行结果
        :param filename: Excel文件名
        :return:
        """
        with xlrd.open_workbook(self.dir_base(filename)) as f:
            work_book=copy(f)#利用xlutils.copy下的copy函数复制
            work_sheet=work_book.get_sheet(0)#获取第一个表单

            style0 = xlwt.easyxf('font: name Times New Roman',
                                 num_format_str='#,##0.00', )  # 字体的颜色
            styleOK = xlwt.easyxf('pattern: fore_colour light_blue;'
                             'font: colour green, bold True;')
            pattern = xlwt.Pattern()  # 一个实例化的样式类
            pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
            
            
            
            if result == 'P':
                pattern.pattern_fore_colour = xlwt.Style.colour_map['red']  # 背景颜色
            if result == 'F':
                pattern.pattern_fore_colour = xlwt.Style.colour_map['green']  # 背景颜色
            styleOK.pattern = pattern
            
            work_sheet.write(row, col, result, styleOK)  # 使用样式
            work_book.save(self.dir_base(filename))

e=OperationExcel()
v=e.getExcelData('data.xls')
print(v)
e.modifyExcel('data.xls',1,3,'P')
# e.modifyExcel('data.xls',2,3,'F')
# e.modifyExcel('data.xls',3,3,'P')