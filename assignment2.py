#:Triangle formation
a=int(input("please enter the first number: "))
b=int(input("please enter the second number: "))
c=int(input(" please enter the third number: "))
if a+b>c and a+c>b and c+b>a:
    print("true")
else:
    print("false")