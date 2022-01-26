import math
#Calculate the Area of triangle using the "Heron's Traingle formula"
a = float(input("Enter a num"))
b = float(input("Enter a num"))
c = float(input("enter a num"))
s = (a + b + c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle",area)






