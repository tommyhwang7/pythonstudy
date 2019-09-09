sum=0
#print (str(num)+"*"+str(num)+"="+str(num*num))
for i in range(1,20):
    if i %3 == 0:
        sum = sum + i
    if i %15 == 0:
        sum = sum - i
        #print (str(i))
print (str(sum))
sum1=0
for j in range(1,21):
    if j %5 == 0:
        sum1 = sum1 + j
    if j %15 == 0:
        sum1 = sum1 - j
        #print (str(j))
print (str(sum1))