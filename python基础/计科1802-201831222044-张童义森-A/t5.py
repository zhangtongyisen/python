import os
print(os.getcwd())
file=open("data.txt","r")
f=file.readlines()
f1=[]
for i in range(len(f)):
    f1.append(int(f[i])-3)
               
f2=open('data_new.txt','w')
for i in range(len(f1)):
    f2.writelines(str(f1[i])+'\n')
    
f2.close()

