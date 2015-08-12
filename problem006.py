__author__ = 'USER'

sumofsqare = 0
sqareofsum = 0
for i in range(1,101):
    sumofsqare = sumofsqare + i**2
    sqareofsum = sqareofsum + i

sqareofsum = sqareofsum ** 2

print ("Difference", sqareofsum-sumofsqare)

