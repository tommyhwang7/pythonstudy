import random

lotto_count=0
lotto_nums=[i for i in range(1,46)]
#print (lotto_nums)


#print (random_num)
lotto_num=[0]*6

for i in range(0,6):
    random_num = random.randrange(len(lotto_nums))
    #print (random_num)
    lotto_num[i] = lotto_nums.pop(random_num)
    

print (sorted(lotto_num))

print (len (lotto_nums))



#Random_num = random.randrange(1,10)

