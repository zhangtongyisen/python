from pylab import *
x=linspace(-1,1,999)
m=[True if(i>3 and i<4) else False for i in x]
y=(-(x**3))*(x<3)+(x+2)*m+sin(x)*(x>4)
plot(x,y)
show()
