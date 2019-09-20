f = open ("99.txt",'r')

lines = f.readlines()

f.close()

count=0

for line in lines:
    count+=1
    if count > 9:
        break
    print (line.strip())
    
'''text = "123456789"
for c in text:
    print (c)'''

target_file = open ("first_multi.txt",'w')

count=0

for line in lines:
    count+=1
    if count > 9:
        break
    data = (line)
    target_file.write(data)

target_file.close()