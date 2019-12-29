Address={}
command={}

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

    if Name0 in Address :
        print (Name0, "phone No is : ", Address[Name0])
        
    else :
        print ("not found")

def InputInform():
    InputName0 = input('Name :')
    Name0 = (InputName0)
    
    for i in range (0,10) :
        if Name0 in Address :
            print ("duplicate name exists, Do you want to overwrite it?")
            InputDicison = input ('y or n : ')
            if InputDicison == ('y') :
                InputPhoneNum0 = input('phone Num :')
                Address[Name0] = InputPhoneNum0
                break
            else :
                break
     
    else :
        InputPhoneNum0 = input('phone Num :')
        Address[Name0] = InputPhoneNum0

def Delete():
    InputName0 = input('Delete Name :')
    Name0 = (InputName0)

    if Name0 in Address :
        del Address[InputName0]
        
    else :
        print ("not found")
    
    
    

def InputSelect():
    for i in range(0,100):
        InputSelect0 = input('input(i) or exit(e) or print(p) or search(s) or del(d) : ')
        
        if InputSelect0 == ('i'):
            InputInform()
        
        elif InputSelect0 == ('e'):
            print ('exit')
            break

        elif InputSelect0 == ('p'):
            print (Address)

        elif InputSelect0 == ('s'):
            Serch()

        elif InputSelect0 == ('d'):
            Delete()
        
            
def test():
    '''Test case'''
    InputInform()
    print (Address)


    #assert NameList == ['sang']
    #print ("Pass!")
    return True

def main():
    InputSelect()
    print (Address)
    


if __name__ == '__main__':
    #test()
    main()