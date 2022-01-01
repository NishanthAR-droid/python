#program to compute area of circle
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius ",r," is: ",pi*(r**2))

#extension program
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + f_extns[1])
