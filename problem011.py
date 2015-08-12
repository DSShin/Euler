__author__ = 'USER'
count = 1
i=0
sum=0

while count < 500:
    count = 2
    i = i+1

    print(i, " : ", end='')

    sum = 0
    for j in range(1,i+1):
        sum = sum + j


    for j in range(1,int(sum**0.5)):
        if sum%j == 0:
            print(j,int(sum/j),' ', end='')
            count = count+2

    print (sum, " count ", count)

print("The first count sum is", sum)

