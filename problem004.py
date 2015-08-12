__author__ = 'USER'

total=0
largest = 0
for i in range(100,1000):
    for j in range(100,1000):
        total = i * j
        total = str(total)
        reverse = ''

        for a in total:
            reverse = a + reverse

        if reverse == total:
            print (i, j, total)
            if int(total) > largest:
                largest = int(total)


print("The Largest palindromc number is ", largest)
