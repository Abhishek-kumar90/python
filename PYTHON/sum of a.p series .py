i = 1
sum = 0
for i in range(1):
    print(2*(i+1),end=" ")
    sum = sum+1
print(sum)
i = i+1

def sumOfAP( a, d,n) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
n = 20
a = 2.5
d = 1.5
print (sumOfAP(a, d, n))


