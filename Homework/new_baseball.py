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



#print (Random_number)

count=1

while True:
    Input_number=[0,0,0]
    Input_number[0]=int(input('inputnumber1 '))
    Input_number[1]=int(input('inputnumber2 '))
    Input_number[2]=int(input('inputnumber3 '))


    strike=0
    ball=0
    out=0
    

    if Random_number[0] == Input_number[0]:
        strike=strike+1
    if Random_number[1] == Input_number[1]:
        strike=strike+1
    if Random_number[2] == Input_number[2]:
        strike=strike+1
    if strike == (3):
        print ('homrun')
        break
    
    if Random_number[0] != Input_number[0] and Random_number[1] == Input_number[0] or Random_number[2] == Input_number[0] :
        ball=ball+1
    if Random_number[1] != Input_number[1] and Random_number[0] == Input_number[1] or Random_number[2] == Input_number[1] :
        ball=ball+1
    if Random_number[2] != Input_number[2] and Random_number[0] == Input_number[2] or Random_number[1] == Input_number[2] :
        ball=ball+1
    
    if strike == (0) and ball == (0):
        print ('out')
       

    print (strike,str('strike'),ball,str('ball'))

   

    count = count+1
    if count>10 or count<1:
        print ('time_over')
        break

    print (str('There are'),11-count, str('chances left'))





