#1-10000까지 숫자 중 3과5의 배수 합을 구하는데 
#15배수는 빼고 그합을 구하시요 _ 20010003
sum=0
for i in range(1,20):
    if (i %15 != 0) and ((i %3 == 0) or (i % 5 == 0)):
        sum = sum + i
        print (i)
print (str(sum))