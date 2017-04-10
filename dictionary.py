# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:28:03 2017

@author: Song
"""
"""
alien_0={'color': 'green','points': 5}#花括号

print(alien_0['color'])
print(alien_0['points'])
"""
"""
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)
"""

alien_0={'x_position':0,'y_position':25,'speed':'medium','color':'green'}
print("Original x-position:" + str(alien_0['x_position']))

alien_0['speed']='fast'

if alien_0['speed']=='slow':
   x_increment=1
elif alien_0['speed']=='medium':
   x_increment=2
else:
   x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position:" + str(alien_0['x_position']))

#del alien_0['color']

favorite_languages={
     'jen':'python',
     'ben':'C',
     'phil':'ruby',
     'edward':'python'}

for key,value in favorite_languages.items():
    print("Key: "+key+"\n")
    print("Value: "+value+"\n")

for languages in set(favorite_languages.values()):
        print(languages.title()+"\n")
        


     
     
     
     
     
     
     
     
     









