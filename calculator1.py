print("=======calculator02=======")

import math

op=input(" please enter op(+,-,*,/,sin,cos,tan,cot,factorial,sqrt): ")
if op=="+" :
    a=int(input("please enter num1:"))
    b=int(input("please enter num2:"))
    cal=a+b
    
if op=="*" :
    a=int(input("please enter num1:"))
    b=int(input("please enter num2:"))
    cal=a*b
    
if op=="-" :
    a=int(input("please enter num1:"))
    b=int(input("please enter num2:"))
    cal=a-b

if op=="/" :
    a=int(input("please enter num1:"))
    b=int(input("please enter num2:"))
    if b==0:
        cal="error!! "
    else:
        cal=a/b

if op=="cos":
    a=int(input("please enter a(degree):"))
    cal=math.cos(math.radians(a))

if op=="sin":
    a=int(input("please enter a(degree):"))
    cal=math.cos(math.radians(a))

if op=="tan":
    a=int(input("please enter a(degree):"))
    cal=math.tan(math.radians(a))

if op=="cot":
    a=int(input("please enter a(degree):"))
    b=math.tan(math.radians(a))
    cal=1/b

if op=="factorial":
    a=int(input("please enter number:"))
    if a <0 :
        cal="Error!!"
    else:
        cal=math.factorial(a)

if op=="sqrt":
    a=int(input("please enter number:"))
    if a <0 :
        cal="Error!!"
    else:
        cal=math.sqrt(a)

print(cal)