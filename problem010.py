__author__ = 'USER'

sum= 2
i = 3
print(" Prime number ", 2)
condition = True
while i<2000000:
    for k in range(2,i):
        if i%k == 0:
            condition = False
            break;
        else:
            condition = True

    if condition == True:
        sum = sum+ i
        print(" Prime number ", i)
    i = i +2

print("Prime total is ", sum)
