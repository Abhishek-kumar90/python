numr=int(input("Enter range:"))

# print("Prime numbers:",end=' ')

for n in range(1,numr):

    for i in range(2,n):

        if(n%i==0):

            break

    else:

        print(n,end=' ')    

a = 0
b = 1
c = 0
# n = int(input("enter a number"))
# print(a)
print(b)

i=1
while(i<=n):
    c = a+b
    print(c,end=' ')
    a = b
    b = c
    c = 0
    i = i+1