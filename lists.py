

lst=[6,34,3,23,2]
print(lst) 
var = lst[1:4]
print(var)

#editing lists values
lst[2]=45
print(lst[2])
print(lst)


#inserting in list
#list_name.insert(position,value)
lst.insert(1,100)
print(lst)

#inserting at last
lst.append(50)
print(lst)

#removing from list
lst.remove(34)
print(lst)
#can also be removed using del
del lst[2]
print(lst)

#removing from last i.e. poping
lst.pop()
print(lst)

#for deleting entire elements or clearing
# lst.clear()
# print(lst)