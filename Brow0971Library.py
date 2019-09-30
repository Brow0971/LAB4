def printinstructions():
   print("Hello")
   print("This program will compute MPG for a car")

def CalculateMPG(miles,gallons):
   MPG = miles // gallons
   return MPG

   printinstructions()
   m = int(input("Please input the number of miles driven:>"))
   print(miles)
   g = int(input("Please input the number of gallons used:>"))
   print(gallons)
   MPG = CalculateMPG(m//g)
   print(MPG)
   print("The total Miles per gallon that was calculated by the equation is M= {1}".format(m,g))

   def printinstructions():
       print("Hello")
       print("This program will convert fahrenheit into degrees")

   def ConvertFahrenheittoC(fahrenheit):
       celsius = (fahrenheit - 32) / 1.8
       return celsius

       printinstructions()

   fahrenheit = int(input('Please enter degrees in fahrenheit:'))
   print(fahrenheit)
   celsius = ConvertFahrenheittoC(fahrenheit)
   print(celsius)
   print("The temperature in celsius is celsius={1})".format(celsius))

from math import pi
def printinstructions():
    print ("Hello")
    print ("This program will calculate the area of a circle")

def CalculatecircumOfCircle(radius):
    circumference = radius * 2 * pi
    return circumference


 printinstructions():
 r = float(input("Input the radius of the circle:>"))
print (radius)
c = CalculatecircumOfCircle(r)
print(circumference)
print("The Circumference of the circle from using the radius is r={1} is {0}".format(c,r))

import math

def printinstructions():
    print("Hello World")
    print(This function will calculate the distance between two points using coordinates)

def calculateDistanceBetweenPoints(x,y,x1,y1):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

   printinstructions()
print calculateDistanceBetweenPoints(x,y,x1,y1)
