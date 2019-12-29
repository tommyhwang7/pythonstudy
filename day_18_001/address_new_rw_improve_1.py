contact = {}
command = {}

def init():
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
    InputName0 = input('Name :')
    Name0 = (InputName0)
    
    for i in range (0,10) :
        if Name0 in contact :
            print ("duplicate name exists, Do you want to overwrite it?")
            InputDicison = input ('y or n : ')
            if InputDicison == ('y') :
                InputPhoneNum0 = input('phone Num :')
                contact[Name0] = InputPhoneNum0
                break
            else :
                break
     
    else :
        InputPhoneNum0 = input('phone Num :')
        contact[Name0] = InputPhoneNum0

def updateContact():
    global contact
    print('updateContact')

def deleteContact():
    global contact
    print('deleteContact')

def searchContact():
    global contact
    print('searchContact')

def printContact():
    global contact
    print(contact)

def run():
    cmd = input('input(i) or exit(e) or print(p) or search(s) or delete(d) : ')
    cmdLowcase =  cmd.lower().strip()

    while True:
        if (cmd == 'q') or (cmd == 'quit'):
            break
        if cmd in command.keys():
            command[cmd]()
        cmd = input('Please input commmand :')
        cmdLowcase =  cmd.lower().strip()
   
def main():
    init()
    run()

def test():
    init()
    command['i']()

if __name__ == '__main__':
    main()
    #test()