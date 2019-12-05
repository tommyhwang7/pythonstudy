
file=open("address.txt","wt") 


a={}

hw = 'hwang'
hy = 'hyun'
No3172 = '3172'

a = { hw:'010','sang':'2060'}
a[hy] = No3172

print (a)

for key in a.keys():
    file.write(key +'\n'+ a[key]+ '\n')


file.close()


