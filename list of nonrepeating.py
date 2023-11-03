import random as rnd
_len=int(input("How long is the list? : "))
_list=[]
counter=0
for i in range (_len):
    new=rnd.randint(0,2000)
    if new not in _list:
        _list.append(new)
        counter+=1
print("Your random  list is:",_list)
print("Frequency of random numbers by module: ",counter)