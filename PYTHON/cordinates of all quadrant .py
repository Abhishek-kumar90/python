a  = int(input())
b = int(input())

if(a>0 and b>0):
    print("1st quadrant")
elif(a<0 and b>0):
    print("2nd quadrant")
elif(a<0 and b<0):
    print("3rd quadrant")
elif(a>0 and b<0):
    print("4th quadrant")
else:
    print("origin")