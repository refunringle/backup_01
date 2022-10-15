a=int(input("enter the side1:"))
b=int(input("enter the side2:"))
c=int(input("enter the side3:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area:",area)
