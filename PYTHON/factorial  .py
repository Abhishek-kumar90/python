# num = int(input("enter a number"))
# fac = 1
# for i in range(1,num+1):
#     fac= fac*i
#     print("factorial of :",num,"is",fac)

# using while loop to print factorial of number

num = int(input("enter a number:"))
i = 1
fac = 1
sum =0
while(i<num):
    fac = fac*i
    i = i+1
sum = sum+fac
print(sum) 
print("factorial of",num,"is",fac)
