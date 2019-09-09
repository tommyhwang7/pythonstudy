def multi_sum(max_num,skip_num,find_num_A,find_num_B):
    sum=0
        
    for i in range(1,max_num):
        multi_skip = (i % skip_num == 0)
        multi_find_A = (i % find_num_A == 0)
        multi_find_B = (i % find_num_B == 0)
        if (multi_skip == False) and (multi_find_A or multi_find_B):
            sum = sum + i
            #print (i)
    print (sum) 


def print_hello():
    print ("helloworld")

print_hello()

multi_sum(10001,20,10,17)
multi_sum(10001,30,11,16)
max_num=input('input max number ')
skip_num=input('input skip number ')
find_num_A=input('input find A number ')
find_num_B=input('input find B number ')

#print(num)
multi_sum(int(max_num),int(skip_num),int(find_num_A),int(find_num_B))