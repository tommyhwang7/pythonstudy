num=1
one=1
#print (str(num)+"*"+str(num)+"="+str(num*num))
for one in range(1,10):
    for num in range(1,10):
        if one*num %2 == 0:
            print (str(one)+"*"+str(num)+"="+str(one*num))
    