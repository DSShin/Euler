__author__ = 'shunaker'
sum = 2
condition = True
for i in range(3,2000000,2):
    for j in range(3,i,2):
        if j>i**0.5:
            break
        else:
            if i%j == 0 :
                condition=False
                break
        condition = True
    if condition == True :
        print("Prime ",i)
        sum = sum + i

print("Total Prime is ", sum)