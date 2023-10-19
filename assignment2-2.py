#calculation of GPA of students:
name=input("please enter first name: ")
family=input("please enter last name: ")
c=int(input("enter the grade of the first lesson: "))
d=int(input("enter the grade of the second lesson: "))
e=int(input("enter the grade of the third lesson: "))
cal=(c+d+e)/3
print(cal)
if cal>=17:
    print("student",name,family,"is great")
elif cal<17 and cal>=12:
    print("student",name,family,"is normal")
else:
    print("student",name,family," is fail")