lst=input()
lst1=lst.split(",")
lst2=[]
for i in range(4):
    lst2.append(int(lst1[i])+int(lst1[i+1]))
for i in range(4):
    if i != 3:
        print(lst2[i], end=",")
    else:
        print(lst2[i], end="")
