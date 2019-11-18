NameList=[]
PhoneList=[]

def InputName():
    InputName0 = input('Name :')
    Name0 = (InputName0)
    NameList.append(Name0)

def InputPhoneNum():
    InputPhoneNum0 = input('phone Num :')
    PhoneNum0 = (InputPhoneNum0)
    PhoneList.append(PhoneNum0)

  

def InputSelect():
    for i in range(0,10):
        InputSelect0 = input('input or exit or print or search or del : ')
        
        if InputSelect0 == ('input'):
            InputName()
            InputPhoneNum()
        
        elif InputSelect0 == ('exit'):
            print ('exit')
            break

        elif InputSelect0 == ('print'):
            print (NameList)
            print (PhoneList)

        elif InputSelect0 == ('search'):
            print ('search')

        elif InputSelect0 == ('del'):
            print ('del')
        
            
            



InputSelect()

print (NameList)
print (PhoneList)


