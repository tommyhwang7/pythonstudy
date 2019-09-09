import random

def random_num():
    new_number=random.randrange(1,10)
    return new_number
#print (random_num())

Random_number=[]

Random_A=random_num()
Random_B=random_num()
Random_C=random_num()

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

'''while True: # 이전 방식
    
    if (Random_A != Random_B) and (Random_A != Random_C) and (Random_B != Random_C):
    Random_number.append(Random_A)
    print(len(Random_number))
    Random_number.append(Random_B)
    print(len(Random_number))
    Random_number.append(Random_C)
    print(len(Random_number))
    break

while True:
    Random_number.append(random_num())
    if Random_number[0] != Random_number[1]:
        break     


while True:
    Random_number.append(random_num())
    if Random_number[0] != Random_number[2] and Random_number[1] != Random_number[2] :
        break'''

print (Random_number)

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





