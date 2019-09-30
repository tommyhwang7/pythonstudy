f = open("99.txt","w")

for one in range(1,10):
    for num in range(1,10): 
        gugu = str(one)+"*"+str(num)+"="+str(one*num) + "\n"
        f.write(gugu)

f.close()

f = open("99.txt","r")
firstLine = f.readline()
print (firstLine)

f.close()

