num = int(input("enter a number"))
sum = 0
temp = num
while(num>0):
    rem = num%10
    sum = sum+rem
    num = num//10
if(temp%sum==0):
    print("is a harsad number")
else:
    print("is not harsad number")
