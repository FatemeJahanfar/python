print("Hello dear,Welcome to the dice game \n ")
import random
while True:
    result=random.randint(1,6) 
    if result==6:
        print("amazing! The Result  is:",result)
        a=random.randint(1,6)
        print("The first chance is:",a)
        b=random.randint(1,6)
        print("The second chance is:",b)
        break
    else:
        print("Result  is:",result)
        break