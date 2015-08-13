__author__ = 'USER'


total = 0
for i in range(1,1001) :
    if i == 1000:
        total = total + 11

    count1 = int(i/100)
    count2 = int((i%100)/10)
    count3 = int(i%10)
    if count1 == 1 or count1 == 2 or count1 == 6 :
        total = total + 13
        if count2 == 0 and count3 == 0 :
            total = total - 3
    elif count1 == 4 or count1 == 5 or count1 == 9:
        total = total + 14
        if count2 == 0 and count3 == 0 :
            total = total - 3
    elif count1 == 3 or count1 == 7 or count1 == 8:
        total = total + 15
        if count2 == 0 and count3 == 0 :
            total = total - 3

    if count2 == 7:
        total = total + 7
    elif count2 == 2 or count2 == 3 or count2 == 8 or count2 == 9 :
        total = total + 6
    elif count2 == 4 or count2 == 5 or count2 == 6 :
        total = total + 5
    elif count2 == 1 :
        if count3 == 0 :
            total = total+3
            print (i, total)
            continue
        elif count3 == 1 or count3 == 2:
            total = total+ 6
            print (i, total)
            continue
        elif count3 == 3 or count3 == 4 or count3 == 8 or count3 == 9:
            total = total + 8
            print (i, total)
            continue
        elif count3 == 6  or count3 == 5:
            total = total + 7
            print (i, total)
            continue
        elif count3 == 7:
            total = total + 9
            print (i, total)
            continue

    if count3 == 1 or count3 == 2 or count3 == 6 :
        total = total + 3
    elif count3 == 4 or count3 == 5 or count3 == 9:
        total = total + 4
    elif count3 == 3 or count3 == 7 or count3 == 8:
        total = total + 5
    print (i, total)



