contact = {}
command = {}

def instruction():
    global command
    command['i'] = createContact
    command['input'] = createContact
    command['e'] = updateContact
    command['edit'] = updateContact
    command['d'] = deleteContact
    command['delete'] = deleteContact
    command['s'] = searchContact
    command['search'] = searchContact
    command['p'] = printContact
    command['print'] = printContact


def createContact():
    global contact
    Name0 = input('name : ')
    if Name0 in contact:
        print ('duplicate name, Wanna overwrite it ?')
        InputDicsion = input ('y or n : ')
        if InputDicsion == ('y') :
            phoneNum = input('phone number :')
            contact[Name0] = phoneNum
        
    else :
        phoneNum = input('phone number :')
        contact[Name0] = phoneNum



def updateContact():
    global contact
    Name0 = input('name : ')
    if Name0 in contact:
        print ('Wanna update it ?')
        InputDicsion = input ('y or n : ')
        if InputDicsion == ('y') :
            phoneNum = input('phone number :')
            contact[Name0] = phoneNum
        
    else :
        phoneNum = input('phone number :')
        contact[Name0] = phoneNum

    
def deleteContact():
    global contact
    Name0 = input('name : ')
    if Name0 in contact :
        del contact[Name0]
    else :
        print ('not found')

    

def searchContact():
    global contact
    Name0 = input('name : ')
    if Name0 in contact :
        print (contact[Name0])
    else :
        print ('not found')

def printContact():
    global contact
    print(contact)

def run():
    cmd = input ('input(i) or edit(e) or print(p) or search(s) or delete(d) or quit(q) :')
    cmdLowcase = cmd.lower().strip()

    for i in range (0,10):
        if (cmdLowcase == 'q') or (cmdLowcase =='quit'):
            break
        if cmdLowcase in command.keys():
            command[cmdLowcase]()
        cmd = input ('input(i) or edit(e) or print(p) or search(s) or delete(d) or quit(q) :')
        cmdLowcase = cmd.lower().strip()




def main():
    instruction()
    run()
    #instruction()
    #print (command)




if __name__ == '__main__':
    main()

