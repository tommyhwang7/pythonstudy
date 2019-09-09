import random

def random_num():
    for i in range(0,1):
        new_number=random.randrange(1,10)
    #print (new_number)
    return new_number

#print (random_num())

Random_A=random_num()
Random_B=random_num()
Random_C=random_num()
print (Random_A,Random_B,Random_C)

while True:
    Input_1=input('inputnum_1 :')
    num_1=int(Input_1)
    Input_2=input('inputnum_2 :')
    num_2=int(Input_2)
    Input_3=input('inputnum_3 :')
    num_3=int(Input_3)

    strike=0
    if Random_A == num_1:
	    strike=strike+1
    if Random_B == num_2:
	    strike=strike+1
    if Random_C == num_3:
	    strike=strike+1

    if strike == (3):
        print ('homerun')
        break

    ball=0
    if Random_A != num_1:
	    ball=ball+1
    if Random_B != num_2:
	    ball=ball+1
    if Random_C != num_3:
	    ball=ball+1
    if ball == (3):
	    print ('out')

    print (strike,str('strike'),ball,str('ball'))

