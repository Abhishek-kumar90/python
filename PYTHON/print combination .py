def fact(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    return(f)

n = int(input("enter a number"))
r = int(input("enter a fac"))
c = (fact(n))/((fact(n-r))*fact(r))
print(c)
