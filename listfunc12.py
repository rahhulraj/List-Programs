mylist=[]

for i in range(10):
    studentname=input("ENTER THE STUDENT NAME : ")
    mylist.append(studentname)

print("STUDENT LIST :", mylist)

newstudent=input("ENTER NEW STUDENT NAME : ")
mylist.append(newstudent)

print("AFTER ADDING NEW STUDENT :", mylist)

anotherstudent=input("ENTER STUDENT NAME TO 3rd POS : ")
mylist.insert(2, anotherstudent)
print("NEW LIST :", mylist)

studerem=input("ENTER THE STUDENT TO BE REMOVED : ")
mylist.remove(studerem)
print("LATEST LIST :", mylist)

newstudent2=input("ENTER THE STUDENT NAME : ")
if newstudent2 in mylist:
    print("STUDENT ENROLLED")
    print(newstudent2, "IS ENROLLED AT POSITION", mylist.index(newstudent2) + 1)
else:
    print("STUDENT NOT ENROLLED")

searchname=input("ENTER STUDENT NAME TO COUNT : ")
print("NUMBER OF TIMES APPEARED :", mylist.count(searchname))

mylist.sort()
print("ALPHABETICAL ORDER :", mylist)

mylist.sort(reverse=True)
print("REVERSE ALPHABETICAL ORDER :", mylist)

mylistcopy=mylist.copy()
print("ORIGINAL LIST :", mylist)
print("COPIED LIST :", mylistcopy)

mylistcopy.clear()
print("AFTER CLEARING COPIED LIST")
print("ORIGINAL LIST :", mylist)
print("COPIED LIST :", mylistcopy)

print("TOTAL NUMBER OF STUDENTS :", len(mylist))
