f = open("99.txt","w")

for one in range(1,10):
    for num in range(1,10): 
        line = str(one)+"*"+str(num)+"="+str(one*num) + "\n"
        f.write(line)

f.close()

