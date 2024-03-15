# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 04:31:14 2024

@author: hp
"""
#list of Dictionarirs
dict2=[{"name":"nidhi",
      "mark1":50,
      "mark2":75,
      "mark3":80 },
      {"name":"khushi",
       "mark1":60,
       "mark2":70,
       "mark3":90}]
print(dict2)
#add a student with their data
dict1={"name":"sonu",
       "mark1":90,
       "mark2":80,
       "mark3":70}
dict2.append(dict1)
print(dict2)
#delete one of the student from list
dict2.pop(1)
print(dict2)
#print Name amd sum of all student marks in list
for i in dict2:
    total=i["mark1"]+i["mark2"]+i["mark3"]
    print(i["name"],total)