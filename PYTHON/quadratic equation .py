a = int(input("enter a value"))
b = int(input("enter b value"))
c = int(input("enter c value"))


d = (b**2)-4*a*c
if(d==0):
    r = -b/2*a
    r1 = -b/2*a
    print(r)
    print(r1)

elif(d>0):
    x = ((-b)+d**0.5)/(2*a)
    x1 = ((-b)-d**0.5)/(2*a)
    print(x)
    print(x1)
else:
    print()
