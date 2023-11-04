m=int(input("what's the row of the board? "))
n=int(input("what's the column of the board? "))
a=[]
for i in range(m):
    row=["*#"]*n
    a+=[row]
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()