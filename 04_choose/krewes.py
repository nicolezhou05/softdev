import random as ran

def devo(diction):
    b = len(diction)
    num = randint(0, b - 1)
    num1 = randint(0, len(diction[num]))
    return diction[num[num1]]
    
krewes = {2:["duck", "bob"], 7:["Thomas", "Nicole"], 8:["software", "development"]}
print(devo(krewes))