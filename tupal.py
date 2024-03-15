# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:19:39 2024

@author: hp
"""

mytupal=("nidhi","khushi","sonu")
print(mytupal)


#add item in tupal
mytupal2=list(mytupal)
mytupal2.insert(2, "aru")
mytupal=tuple(mytupal2)
print(mytupal)

#print the tupal in second postion
print(mytupal[1:])

#revers print tupal
for i in reversed(mytupal):
    print(i)
print(mytupal[::-1])
    
    
#loop through tupal
for i in range(len(mytupal)):
    print(mytupal[i])
    
        
    
