import sys
from fileinput import filename

print("#program to calculate area of circle using radius as a input.\n")
radius=float(input("Enter the radius of circle:\n"))
area = 3.14*radius*radius
radius=str(radius)
area=str(area)
print("the area of circle with "+radius+ " is: " +area)

print("###################################################################\n")

print("#program to print extension of a filename.")

fileName=input("Enter the filename with extension:\n")


if '.py' in fileName:
    print("python")
else:
    print("enter valid extension")
