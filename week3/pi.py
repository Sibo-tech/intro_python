from math import sqrt

root = 2*(2/sqrt(2))
denom = sqrt(2)
pi = root
while 2 / sqrt(2 + denom) > 1:
    pi = pi * 2 / sqrt(2 + denom)
    denom = sqrt(2 + denom)
print("Approximation of pi: %s" % (round(pi, 3)))

r = float(input("Enter radius: \n"))
r=r*r
A= pi*r
A=round(A,3)
print("Area: "+str(A))