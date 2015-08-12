__author__ = 'USER'
a=1
b=1
c=1
while a< 1000:
    while b < 1000:
        if a>b:
            b=b+1
            c=1
            continue
        else :
            while c < 1000:
                if a>b or a>c or b>c :
                    c=c+1
                    continue
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2 :
                        print(a, b, c, a*b*c)
                #print(a,b,c)
                c=c+1
            b=b+1
            c=1
    a=a+1
    b=1
    c=1


