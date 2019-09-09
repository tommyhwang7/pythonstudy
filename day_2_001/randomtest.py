import random

num=[]

for i in range(0,7):
    new_number=random.randrange(1,10)
    print (new_number)
    num.append(new_number)
    print (num)
    #print (num[i])

print (num[7])