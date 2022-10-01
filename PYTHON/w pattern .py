
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")

    for abhi in range(10-2*i,0,-1):
        print(' ',end="")

    for k in range(j,0,-1):
        print(k,end="")
    print()