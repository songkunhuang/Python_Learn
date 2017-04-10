# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:49:58 2017

@author: Song
"""
"""
cars=['Bmw','bmw','audi','honda','toyota']

for car in cars:
        if car=='bmw': #更严谨的写法 if car.lower()=='bmw'
                print(car.upper())
        else:
                print(car.title())
"""
# 布尔表达式
# 多个条件 and 、 or  不等关系!=
"""
requested_toppings=['mushroms','onions','pineapple']
print('mushroms' in requested_toppings)#判断是否包含，不包含 not in
print(requested_toppings=='mushroms')
print('Mushroms' not in requested_toppings)
print('Mushroms' in list(top.title() for top in requested_toppings))#列表解析
"""
# if-else
# if-elif-else
# if-elif-elif
# if-if-if
"""
#if处理列表
requested_toppings=['mushroms','onions','pineapple']
for requested_topping in requested_toppings:
        if requested_topping=='mushroms':
           print("Sorry,we are out of mushroms right now")
        else:
           print("Add "+requested_topping)
print("\nFinished making your pizza.")

#判断是否为空列表
empty_list=[#0,1,2,3
            ]
if empty_list:
        print("Not Empty.")
else:
        print("Empty.")
"""
"""#多表互动
available_toppings=['mushroms','olives','green peppers','pepperoni','pineapple',
                    'extra cheese']
requested_toppings=['mushroms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
            print("Adding ",requested_topping)
    else:
            print("Sorry, we don\'t have "+requested_topping)
print("Finished making your pizza.")
"""

"""
user_list=['wlx','skh','gwp','','gyp','cj','Admin','']
for user in user_list:
        
        if user.lower()=='admin':
           print("Hello administrator, would you like to see a status report?")
        elif user:
           print("Hello "+user+", thank you for logging again.")
        else:
           print("Please input your username!")
"""

current_users = ['Wlx', 'skh', 'gwp', 'gyp', 'cj', 'Admin']
current_users = list(current_user.lower() for current_user in current_users)
new_users = ['wlX', 'cj', 'lyw']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " has been used.")
    else:
        print(new_user + " can be used")

user_list = ['', '']
if user_list:
    for user in user_list:
        if user.lower() == 'admin':
            print("Hello administrator, would you like to see a status report?")
        elif user:
            print("Hello " + user + ", thank you for logging again.")
        else:
            print("Please input your username!")
else:
    print("user_list is empty.")
