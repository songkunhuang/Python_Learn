# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:20:47 2017

@author: Song
"""
""" #大小写转换
message="Hello world"
print(message)
message="I like python"
print(message.title())
print(message.upper())
message=message.upper()
print(message.lower())
"""

"""#语句拼接
first_name="Song"
last_name="Kun-huang"
full_name=first_name+" "+last_name
print(full_name)
"""

"""#转义字符
print("Hello,\tPython\n")
print("Which computer language do you like?\n\tC\n\tJava\n\tR\n\tPython\n\t")

message="What's your name?"
print(message)
message='What\'s your name?'
print(message)
"""

"""#字符串空白的处理
favorite_language='  Python  '
print(favorite_language)
print(favorite_language.rstrip())#删除结尾的空白right
print(favorite_language.lstrip())#删除开头的空白left
print(favorite_language.strip())#删除两端的空白string
"""


"""综合应用
last_name="Einstein"
first_name="albert"
famous_person=first_name.title()+" "+last_name
famous_saying="\"A person who never made a mistake never tried anything new.\""
message=famous_person+" once said, "+famous_saying
print(message)
"""

"""
3**2#幂运算**
0.1+0.1
0.2+0.1==0.3
3/2
print(5+3)
"""


"""#类型转换
age=23
message="Happy "+ str(age) + "rd Birthday!"
print(message)
"""

"""#列表
bicycle=['trek','cannondable','redline','specialized']
print(bicycle[0])
print(bicycle[-1])###最后一个元素
print(bicycle[0].upper())
print("The forth band of bicycle is",bicycle[3],".")
bicycle[0]='Adidas'#修改元素
bicycle.append('addbands')#末尾添加元素
print(bicycle)
"""

"""#动态创建列表
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(1,'addmotor')#插入，数字表示插入元素在插入后的角标，如：0表示开头
print(motorcycles)

del motorcycles[0]#删除元素

poped_motorcyles=motorcycles.pop()#把末尾弹出，列表类似“栈”
print(poped_motorcyles)
print(motorcycles)
motorcycles.pop(0)#弹出指定位置的元素

bicycle.remove('redline')#移除指定值,不存在会报错,而且对重复数据只删除一次
print(bicycle)
"""

"""#排序
cars=["BMW","Benz","Honda","Toyota","Audi"]
cars.sort(reverse=True) #降序排列,修改是永久的 tips:"True" not "TRUE"、"true"
print(cars)

cars=["BMW","Benz","Honda","Toyota","Audi"]
print(sorted(cars,reverse=True))#临时排序
print(cars)


cars=["BMW","Benz","Honda","Toyota","Audi"]
print(sorted(cars,reverse=True))#临时排序
print(cars)

cars.reverse()
len(cars)
"""




















