print("\t\t\t\tMultiplication Table\n")
a=[]
b=[]
def multiply():
    m=int(input("How many columns does your table have? "))
    n=int(input("How many rows does your table have? "))
    for i in range (1,m+1):
        print(i,end="\t")
    print()
    print("________________________________________________________________________________________\n")

    for j in range(1,m+1):
        for k in range(1,n+1):
            print(j*k,end="\t")
        print("\n")
if a ==0 or b==0 :
    print("Error!because m,n>0 (: ")
else:
    multiply()