# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:31:34 2017

@author: Song
"""

#不可变的列表称为元组，元组用圆括号定义

dimensions=(10,20,30)
print(dimensions[1])
#dimensions[1]=50 #元素无法赋值，但元组可重新定义
dimensions=(10,20,40)#可重新定义
print(dimensions)




#代码规范：
#缩进4格；行长小于80字符；适当的空行；PEP 8 规范；
