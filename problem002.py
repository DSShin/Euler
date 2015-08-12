__author__ = 'USER'
num1=1
num2=2
num3=0
result=2
while (num3<4000000):
    num3 = num1 + num2
    #print(num3)
    num1 = num2
    num2 = num3
    if num3%2==0:
        result = result+num3

print(result)
