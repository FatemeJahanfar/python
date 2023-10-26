import random
ModuleNumber=random.randint(0,10)
count=0
while True :
    userguess=int(input("Enter the number you guess: "))
    count=count+1
    if userguess==ModuleNumber:
        print("Great(: ")
        break
    if  userguess<ModuleNumber:
        print("ModuleNumber>your guess! Try again")
    if userguess>ModuleNumber:
        print("ModuleNumber<your guess")
print("ModuleNumber=",ModuleNumber)
print("The number of userguess entered =",count)