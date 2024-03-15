# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 22:47:41 2024

@author: hp
"""
#add item in list using fuction
def add_item(value):
    student_list.append(value)
    
student_list=["nidhi","khushi","sonu"]
add_item("aru")
print(student_list)
    
#first position add to itme in list
def add_first_position_item(index,value):
    student_list.insert(index, value)
student_list=["nidhi","khushi","sonu"]
add_first_position_item(0,"yashana")
print(student_list)

#last position add item in list
def add_last_position_item(value):
    student_list.insert(len(student_list), value)
student_list=["nidhi","khushi","sonu"]   
add_last_position_item("yash")
print(student_list)

#add item in mid position in list
def  add_mid_position_item(value):
    student_list.insert(len(student_list)//2, value)
student_list=["nidhi","khushi","sonu"]     
add_mid_position_item("janki")
print(student_list)

#replace any existing item
def replace_item(value):
    student_list[2]=value
student_list=["nidhi","khushi","sonu"]      
replace_item("anchal")
print(student_list)
    
#print from end to begining
def revers_list(student_list):
    for student_list in reversed(student_list):
        print(student_list)
 
student_list=["nidhi","khushi","sonu"]    
revers_list(student_list)

#print from second element to last second
def show_item_second(student_list):
    print(student_list[1:-1])
   
    
student_list=["nidhi","khushi","sonu","manshi","devashi","jinal"]
show_item_second(student_list)    


    
    
    
    
 