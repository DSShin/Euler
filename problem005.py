__author__ = 'USER'

total = 1
large = int(input("Please input Large Number "))
smallmult = 0
condition = False
for i in range(1,large+1):
    total = total * i

for j in range(1, total):
    for k in range(1,large+1):
        if j%k != 0:
            condition = False
            break
        else :
            condition = True

    if condition == True:
        print (j)
        exit(0)





print(total)