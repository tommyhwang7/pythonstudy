import random

def random_num():
    new_number=random.randrange(1,10)
    return new_number
#print (random_num())

Random_number=[]
Random_number.append(random_num())

while True:
    Random_number.append(random_num())
    if Random_number[0] != Random_number[1]:
        break     


while True:
    Random_number.append(random_num())
    if Random_number[0] != Random_number[2] and Random_number[1] != Random_number[2] :
        break

print (Random_number)


while True:
    Input_number=[0,0,0]
    Input_number[0]=int(input('inputnumber1 '))
    Input_number[1]=int(input('inputnumber2 '))
    Input_number[2]=int(input('inputnumber3 '))


    strike=0
    if Random_number[0] == Input_number[0]:
        strike=strike+1
    if Random_number[1] == Input_number[1]:
        strike=strike+1
    if Random_number[2] == Input_number[2]:
        strike=strike+1
    if strike == (3):
        print ('homrun')
        break
    
    ball=0
    if Random_number[0] != Input_number[0]:
        ball=ball+1
    if Random_number[1] != Input_number[1]:
        ball=ball+1
    if Random_number[2] != Input_number[2]:
        ball=ball+1
    if ball == (3):
        print ('out')

    print (strike,str('strike'),ball,str('ball'))





