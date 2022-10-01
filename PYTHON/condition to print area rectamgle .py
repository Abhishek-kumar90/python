r = int(input("enter a radius"))
s = int(input("enter a side"))
l = int(input("enter a length"))
w = int(input("enter a widgth"))
b = int(input("enter a base"))
h = int(input("enter a heigth"))
c=int(input("enter a number"))
if(c==0):
    print("area of circle:",4*3.14*r**2)
elif(c==1):
    print("area of square:",s**2)
elif(c==2):
    print("area of rectangle:",w*l)
elif(c==3):
    print("area of traingle:",0.5*h*b)
elif(c==4):
    print("area of circle:",4*3.14*r**2)
    print("area of square:",s**2)
else:
    print("area of circle:",4*3.14*r**2)
    print("area of square:",s**2)
    print("area of rectangle:",w*l)
