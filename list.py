list=["nidhi","khushi","sonu","yashana"]
list.append("aru")
print(list,"1")

#add item in list as first position
list.insert(0, "janki")
print(list,"2")

#add item in list as last position
list.insert(len(list), "mansi")
print(list,"3")

#add item in list as mid position
list.insert (len(list)//2, "sgwu")
print(list,"4")

#replace any existing item
list[2]="nnnn"
print (list,"5")

#print from begining to end
list[:]
print(list,"6")

#print from end to begining
for list in reversed(list):
    print(list)  

#print from second element to last second
list=["nidhi","khushi","sonu","yashana"]
print(list[1:-1])
