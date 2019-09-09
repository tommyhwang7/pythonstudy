import random

def random_num():
    new_number=random.randrange(1,10)
    return new_number
#print (random_num())

Random_number=[]


Random_A=1
Random_B=1
Random_C=0

count=0

while True:
    count = count+1
    if count>10000:
        print ('error')
        break

    Random_A=random_num()
    Random_B=random_num()
    Random_C=random_num()    
    
    if (Random_A != Random_B) and (Random_A != Random_C) and (Random_B != Random_C):
        Random_number.append(Random_A)   
        Random_number.append(Random_B)
        Random_number.append(Random_C)
        break
    
    