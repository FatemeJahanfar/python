print("=======calculator02=======")
import math
while True:
    op=input(" please enter op(+,-,*,/,sin,cos,tan,cot,factorial,sqrt)or exit:")
    if op=="exit":
        break
    if op=="+" :
        a=int(input("please enter num1:"))
        b=int(input("please enter num2:"))
        print(a+b)
    if op=="*" :
        a=int(input("please enter num1:"))
        b=int(input("please enter num2:"))
        print(a*b)
    if op=="-" :
        a=int(input("please enter num1:"))
        b=int(input("please enter num2:"))
        print(a-b)
    if op=="/" :
        a=int(input("please enter num1:"))
        b=int(input("please enter num2:"))
        if b==0:
            print("error!! ")
        else:
            print(a/b)
    if op=="cos":
        a=int(input("please enter a(degree):"))
        print(math.cos(math.radians(a)))
    if op=="sin":
        a=int(input("please enter a(degree):"))
        print(math.sin(math.radians(a)))
    if op=="tan":
        a=int(input("please enter a(degree):"))
        print(math.tan(math.radians(a)))
    if op=="cot":
        a=int(input("please enter a(degree):"))
        b=math.tan(math.radians(a))
        print(1/b)
    if op=="factorial":
        a=int(input("please enter number:"))
        if a <0 :
            print("Error!!")
        else:
            print(math.factorial(a))
    if op=="sqrt":
        a=int(input("please enter number:"))
        if a <0 :
            print("Error!!")
        else:
            print(math.sqrt(a))