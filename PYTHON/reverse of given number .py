num = int(input("enter a number"))#123
reverse = 0
while(num!=0):
    rem= num%10#3,2,1
    reverse = reverse*10+rem#3,2,1
    num= num//10#12,1,0
print("reverse number is:",reverse)