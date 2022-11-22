import random
x=[]
for i in range(50):
    x.append(random.randint(0,100))
x=[i for i in x if i%2==0]
print(x)
