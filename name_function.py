# -*- coding: utf-8 -*-
"""
Created on  16:21 2017/4/12 
@author: Song
@E-mail: songkunhuang@163.com

"""
print("Enter 'q' at any time to quit.")


def get_formatted_name(first, last):
    """Get first name & last name, then generate a formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

while True:
    first = input("Please input your first name: ")
    if first == 'q':
        break
    last = input("Please input your last name: ")
    if last == 'q':
        break
    full_name = get_formatted_name(first, last)
    print("Full name is : " + full_name)

