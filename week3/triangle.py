a= int(input("Enter the length of the first side: "))
b= int(input("Enter the length of the second side: "))
c= int(input("Enter the length of the third side: "))
s=(a+b+c)/2
import math
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print ("The area of the triangle with sides of length "+str(a)+ " and " + str(b) +" and "+ str(c) +" is "+str(area)+".")
