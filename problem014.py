__author__ = 'USER'

start = 1
longstart = 1
longcount = 1
for i in range(1,1000000):
    start = i
    if i == 1 :
        print (1, "Count is : 1")
    else:
        print (i, " -> ", end='')
    count = 1
    while(i!=1):
        if i%2 == 0 :
            i = int(i/2)
            if i == 1 :
                count = count + 1
                print(i, "Count is : ", count)
            else:
                print (i, " -> ", end='')
                count = count + 1
        else :
            i = i*3 + 1
            print (i, " -> ", end='' )
            count = count + 1

    if count > longcount :
        longstart = start
        longcount = count
    print("-----------------------------------------------------------------------------------------------")

print ("Longest chain Staring is ", longstart)