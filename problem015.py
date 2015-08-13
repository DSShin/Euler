__author__ = 'USER'
# x * y lattice -> (x+y)! / (x!*y!)

x = 20
y = 20

xfact = 1
yfact = 1
b= 1

for i in range(1,x+1):
    xfact= xfact*i

for i in range(1,y+1):
    yfact= yfact*i


for i in range(1,x+y+1):
    b= b * i

a = xfact * yfact
c = b/a

print (c)