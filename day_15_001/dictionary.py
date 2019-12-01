a={}

hw = 'hwang'
hy = 'hyun'
No3172 = '3172'

a = { hw:'010','sang':'2060'}
a[hy] = No3172

if "sang" in a :
    print (a["sang"])
    print (a[hw])
else :
    print ("not")

print (a)

del a[hw]
print (a)

a.clear()
print (a)