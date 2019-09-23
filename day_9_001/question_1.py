def checkbrace(data):
    compare=[]
    for c in data:
        if c == '(' :
            compare.append('(')
        else:
            if len(compare) == 0:
                print ("fail")
                return 
            compare.pop()
        
    if len(compare) == 0:
        print ("pass")
    else:
        print ("fail")



f = open ("stack_1.txt",'r')

lines = f.readlines()

f.close()

line_count=int(lines[0])
#print (line_count)

for lineNum in range(1,line_count+1) :
    templine = lines[lineNum]
    checkbrace(templine)


#compare1=[]



    
    
    






'''target_file = open ("result.txt",'w')

count=0

for line in lines:
    count+=1
    if count > 7:
        break
    data = (line)
    target_file.write(data)

target_file.close()'''