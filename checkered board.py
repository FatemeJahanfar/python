n=int(input("what's the row of the board? :"))
m=int(input("what's the column of the board? :"))
_list=[]
for i in range(n):
    for j in range(m):
        if(i+j)%2==0:
            print("#",end="")
        else:
            print("*",end=" ")
    print()