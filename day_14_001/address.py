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

def Serch():
    InputName0 = input('Name :')
    Name0 = (InputName0)

    if Name0 in NameList :
        print (NameList.index(Name0))
        print (PhoneList[NameList.index(Name0)])
    else :
        print ("not found")

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
            Serch()

        elif InputSelect0 == ('del'):
            print ('del')
        
            
def test():
    '''Test case'''
    NameList=["hwang","sang","hyun"]
    PhoneList=["010","2060","3172"]
    assert "sang" in NameList
    if "sang" in NameList :
        print (NameList.index("sang"))
        print (PhoneList[NameList.index("sang")])
    else :
        print ("not found")


    #assert NameList == ['sang']
    #print ("Pass!")
    return True

def main():
    InputSelect()

    print (NameList)
    print (PhoneList)


if __name__ == '__main__':
    test()
        #main()