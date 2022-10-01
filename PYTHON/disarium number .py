# Write a program program to check if the given number is a Disarium Number (11+ 72 + 53 = 1+ 49 + 125 = 175).

num = int(input("enter a number"))
num1 = num 
num2 = num
s = 0
c = 0

while(num!=0):
    num=num//10
    c+=1
print("count",c)

while(num1!=0):
    r = (num1%10)
    d = r**c
    s = s+d
    num1 = num1//10
    c-=1
if(num2==s):
    print("s is disarium number")
else:
    print("not disarium number")