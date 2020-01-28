
n=100

result=[0,1]

while 1:
    temp = result[-1]+result[-2]
    if temp < n: 
        result.append(temp)
    else:
        break

print(result)


