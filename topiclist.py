"""

my_list=[1,2,3,4,5,6,7,8]
print(my_list)
print(type(my_list))
print(my_list[1])
print(my_list[0:4])
print(my_list[2:5])
print(my_list[:4])
print(my_list[::-1])
print(my_list[0:7:2])
print(my_list[-8])
print(my_list[0::2])

"""
""""
my_list=[1,2,3,4,5,6,7,8]
my_list1=[11,12,13,14]
my_liststring=["abcd","fgh","tfhnk","tfyuhkdi","astyu","qwertyu"]
print(my_list)
my_list.insert(8,9)
my_list.append(100)
my_list.extend(my_list1)
my_list.remove(100)
my_list.pop(8)
my_list.pop()
del my_list[8]
#my_list.clear()
my_list.sort(reverse=True)
my_liststring.sort()
print(my_list)
print(my_liststring)

"""

my_list=[1,2,3,4,5,6,7,8]
newlist=list(my_list)
my_list.append(59)
print(newlist)