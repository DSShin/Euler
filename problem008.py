__author__ = 'USER'
strlist = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
largest = 0
num1=0
num2=0
num3=0
num4=0
num5=0
num6=0
num7=0
num8=0
num9=0
num10=0
num11=0
num12=0
num13=0
for i in strlist :
    num1 = int(i)
    total = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 *num13
    if total > largest :
        largest = total

    num13 = num12
    num12 = num11
    num11 = num10
    num10 = num9
    num9 = num8
    num8 = num7
    num7 = num6
    num6 = num5
    num5 = num4
    num4 = num3
    num3 = num2
    num2 = num1

print ("The Largest product is ",largest)

