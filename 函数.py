# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:34:51 2018
练习题5：
1.优化代码 用函数的方式修改练习4
2.打印温度折线图，使用函数来优化(必须有返回值)
函数：
变量（生命周期）
函数的语法1*()
def 函数名():
     指令集合
函数的语法2(有参数的函数)
def 函数名(a,b,c,e)
    指令集合(a)
    指令集合(b,c,e)
函数的语法3（函数的返回值=结果）

@author: root
"""
a=3 ############全局变量
def calc():
    b=4#一定需要缩进！！！局部变量在生命周期在缩进内
    print(b)
calc()
#print(b)  局部变量打印无效
'''
函数的参数说明 鼠标在参数内+快捷键 ctrl i
'''
#################函数语法2
def calc(a,b):
    print('a和b相加是：'+str(a+b))
calc(3,4)
print(calc(3,4))# 没有返回值  
#####################函数的语法3(函数的返回值=结果)"
def calc(a,b,c):
    return a+b+c
print(calc(1,2,3)) 