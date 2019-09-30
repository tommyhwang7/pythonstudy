
f=open("99.txt",'w')

for num in range(2,10):
    for inc in range(1,10):
        result = str(num)+"*"+str(inc)+"="+str(num*inc) + ('\n')
        f.write(result)

f.close()

f1 = open("99.txt","r")

lines = f1.readlines()

f1.close()

for line in range (1,9):
    line=line+1

print (lines[line])


'''
count=0
for line in lines:
    count=count+1
    if count >=10 :
        break
print (line)
'''
'''
count=0
while True:
    count=count+1
    
    if count >=9 :
        break

print (lines[count])
'''
    




    

    

