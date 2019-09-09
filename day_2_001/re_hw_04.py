#1~10000 중 10의배수 와 17의 배수 의 합을 구하는데
#20의 배수는 뺀다.
sum=0
max_num = 10001
skip_num = 20
find_num_A = 10
find_num_B = 17
for i in range(1,max_num):
    multi_skip = (i % skip_num == 0)
    multi_find_A = (i % find_num_A == 0)
    multi_find_B = (i % find_num_B == 0)
    if (multi_skip == False) and (multi_find_A or multi_find_B):
        sum = sum + i
        #print (i)
print (sum) 