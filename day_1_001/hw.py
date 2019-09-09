sum=0
for i in range(1,10001):
    if i %3 == 0:
        sum = sum + i
    if i %15 == 0:
        sum = sum - i
#print (str(sum))
sum1=0
for j in range(1,10001):
    if j %5 == 0:
        sum1 = sum1 + j
    if j %15 == 0:
        sum1 = sum1 - j
#print (str(sum1))
print (str(sum+sum1))