print("hello")
print("world")
print(1234)
print("hello"+"world")
print("hello"+"world"+"123")
print("hello"+"world"+str(123))
print("hello"+"world"+str(456))
print(4*5+3*4)
four=4
num=1
for num in range(1,10):
    #print(num)
    print(str(four)+"*"+str(num)+"="+str(four*num))
five=5
num=1
for num in range(1,10):
    #print(num)
    print(str(five)+"*"+str(num)+"="+str(five*num))

one=1
num=1
for one in range(11,20):
    for num in range(1,10):
        #print(num)
        if one*num % 2 != 0:
            print(str(one)+"*"+str(num)+"="+str(one*num))