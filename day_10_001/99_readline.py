
f=open("99.txt",'w')

for num in range(2,10):
    for inc in range(1,10):
        result = str(num)+"*"+str(inc)+"="+str(num*inc) + ('\n')
        f.write(result)

f.close()

f1 = open("99.txt","r")


for i in range (1,11):
    firstLine = f1.readline()

print (firstLine)
    

'''count=0
while True:
    count=count+1
    firstLine = f1.readline()
    print (count)
    if count >= 10:
        break

print (firstLine)'''

f1.close()


    

    

