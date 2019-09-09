#컴퓨터가 1-10사이에 숫자를 만들면
#사람은 이것을 맞춘다

import random

for i in range(0,1):
    new_number=random.randrange(1,10)
    print (new_number)
    


input_num=input('input number')
print (input_num)

if new_number == int(input_num):
    print ('yes')
else:
    print ('no')
print ('random no is')
print ( new_number)
