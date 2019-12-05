import pickle

file=open("address","wb") 


a={}

hw = 'hwang'
hy = 'hyun'
No3172 = '3172'

a = { hw:'010','sang':'2060'}
a[hy] = No3172

print (a)

pickle.dump(a,file) 
file.close()

file=open("address","rb") 
content=pickle.load(file)

print (content)

