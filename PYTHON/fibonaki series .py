
a = 0
b = 1
c = 0
n = int(input("enter a number"))
# print(a)
print(b)

i=1
while(i<=n):
    c = a+b
    print(c)
    a = b
    b = c
    c = 0
    i = i+1