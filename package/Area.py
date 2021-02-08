#D:\ANAGHA\zzzz\package\Area.py

from Graphics.RectFunctions import*
from Graphics.CirFunctions import*
from Graphics.DGraphis.SphereFunctions import*
from Graphics.DGraphics.CuboidFunctions import*

l=int(input("enter 1"))
b=int(input("enter b"))
print("area = ",RectArea(l,b))
printf("Perimetern=", RectPerimeter(l,b))

r=int(input("enter the radius of circle"))
print("Circle area =",CirArea(r))
print("Circle perimeter =", CirPerimeter(r))

r=int(input("enter radius of sphere"))
print("Circle area = ",SpArea(r))
print("Circle perimeter =", SpPerimeter(r))
