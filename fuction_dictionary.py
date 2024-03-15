# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:54:26 2024

@author: hp
"""
#add a student with their data
def add_data_dictinary(value):
    dict2.append(value)
    print(dict2)
    
    
dict2=[{"name":"nidhi","mark1":50, "mark2":75,"mark3":80 },{"name":"khushi", "mark1":60,"mark2":70, "mark3":90}]
add_data_dictinary({"name":"sonu","mark1":90,"mark2":80,"mark3":70})

#delete one of the student from list
def delete_list(value):
    dict2.remove(value)
    print(dict2)

dict2=[{"name":"nidhi","mark1":50, "mark2":75,"mark3":80 },{"name":"khushi", "mark1":60,"mark2":70, "mark3":90}]    
delete_list(dict2[1])    

#print Name amd sum of all student marks in list
def sum_dict(value):
    for i in value:
        total=i["mark1"]+i["mark2"]+i["mark3"]
        print(i["name"],total)
    
dict2=[{"name":"nidhi","mark1":50, "mark2":75,"mark3":80 },{"name":"khushi", "mark1":60,"mark2":70, "mark3":90}]    
sum_dict(dict2)