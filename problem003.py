__author__ = 'USER'

goal=int(input("insert number!"))
prime = 1
for i in range(1,goal):
    if goal%i == 0 :
        if i>prime :
            condition = True
            print (i)
            for j in range(2,i):
                if i%j==0:
                    condition = False
            if condition:
                prime = i

print(prime)
