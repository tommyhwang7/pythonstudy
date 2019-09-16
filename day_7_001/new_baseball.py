import random

'''def random_num():
    new_number=random.randrange(1,10)
    return new_number
print (random_num())'''

Random_number=[]
Random_num_list=[1,2,3,4,5,6,7,8,9]
First_num = random.randrange(1,10)
Random_number[0]= Random_num_list[First_num]
del Random_num_list [First_num]

print (Random_num_list)