__author__ = 'USER'

count = 1

i = 3
print(count, " Prime number ", 2)
condition = True
while count < 10001:
    for k in range(2,i):
        if i%k == 0:
            condition = False
            break;
        else:
            condition = True

    if condition == True:
        count = count + 1
        print(count, " Prime number ", i)
    i = i +2


