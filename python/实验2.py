import math
x=float(input())
if(x<0):
     y=-x
elif 0<=x<1:
     y=math.sin(2*x)
elif 1<=x<5:
     y=math.sqrt(x**3+x)
elif 5<=x:
      y=2*x+10.5
print(round(y,3))
