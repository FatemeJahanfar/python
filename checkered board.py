m=int(input("what's the length of the board? "))
n=int(input("what's the wide of the board? "))
_list=[]
for j in range(n):
    for i in range(m):
        print("▢", end=" ")
    print()