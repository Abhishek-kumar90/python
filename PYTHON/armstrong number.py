num = int(input("enter a number"))
sum = 0 
i =1
while(i<=num):
    rem = num%10
    sum = sum+(rem**3)
    num = num//10
if(num==sum):
    print("is armstrong number")
else:
    print("is not armstrong")

# using forloop find armstrong

# n = int(input("enter a number"))
