import random
print("Hello dear,Welcome to the dice game \n ")
TASS_1="""
┌---------┐
|         |
|    O    |
|         |
└---------┘
"""
TASS_2="""
┌---------┐
|         |
|  O   O  |
|         |
└---------┘
"""
TASS_3="""
┌---------┐
|         |
|O   O   O|
|         |
└---------┘
"""
TASS_4="""
┌---------┐
| O     O |
|         |
| O     O |
└---------┘
"""
TASS_5="""
┌---------┐
| O     O |
|    O    |
| O     O |
└---------┘
"""
TASS_6="""
┌---------┐
| O     O |
| O     O |
| O     O |
└---------┘
"""
while True:
    print("choose a Option:\n1)start Game Dice\n2)Exit")
    choice=input("Enter a choose: ")
    if choice=="2":
        print("Good bye")
        break
    result=random.randint(1,6)
    if choice=="1" and result==6:
        print(TASS_6)
        a=random.randint(1,6)
        print("The first chance is:",a)
        b=random.randint(1,6)
        print("The second chance is:",b)
    elif choice=="1" and result==5: 
        print(TASS_5)
    elif choice=="1" and result==4:
        print(TASS_4)
    elif choice=="1" and result==3:
        print(TASS_3)
    elif choice=="1" and result==2:
        print(TASS_2)
    elif choice=="1" and result==1:
        print(TASS_1)