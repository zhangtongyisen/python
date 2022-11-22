sum=0
h=100
for i in range(10):
    sum+=h
    h=h/2
    sum+=h
sum-=h
print(sum,h)
