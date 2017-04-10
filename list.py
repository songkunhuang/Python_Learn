# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:43:23 2017

@author: Song
"""
"""#操作列表
magicians=['Alice','David','Bob','Tom']
for magician in magicians:##最后magician赋值为magicians[-1]
        print(magician)
print("Complete!")#缩进管理
#Standar Form
#for item in list_of_items:
"""
        
"""#数值列表
for value in range(1,5):
        print(value)
        
number=list(range(1,6,2))

squares=[]
for value in range(1,11):
        squares.append(value**2)
print(squares)

digits=list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))
"""

"""#列表解析
squares=[i**2 for i in range(1,11)]
print(squares)
"""

#列表切片
players=['charles','martina','contanna','abanda','florence','elegant']
print(players[0:3])
print(players[:3])
print(players[3:])
print(players[-3:])

for players in players[:]:
        print(players.title())

        
#使用切片创建列表副本,直接赋值将导致引用传递
a=[1,2,3]
b1=a
b2=a[:]
a.append(4)
print(b1)#对a的操作影响了b1但对b2无影响
print(b2)#对a的操作影响了b1但对b2无影响























