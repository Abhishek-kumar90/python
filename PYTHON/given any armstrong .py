num = int(input("enter a number"))
i = 1
sum = 0
while(i<=num):
    rem = num%10
    sum = sum+i
    num = num//10
if(sum==num):
    print("armstrong number")
else:
    print("not armstrong number")