contact = {}
command = {}
​
def init():
    global command
    command['i'] = createContact
    command['input'] = createContact
    command['e'] = updateContact
    command['edit'] = updateContact
    command['d'] = deleteContact
    command['delete'] = deleteContact
    command['s'] = deleteContact
    command['search'] = searchCotact
​
def createContact():
    global contact
    print('createContact')
​
def updateContact():
    global contact
    print('updateContact')
​
def deleteContact():
    global contact
    print('deleteContact')
​
def searchCotact():
    global contact
    print('searchCotact')
​
def run():
    cmd = input()
    cmdLowcase =  cmd.lower().strip()
​
    while True:
        if (cmd == 'q') or (cmd == 'quit'):
            break
        if cmd in command.keys():
            command[cmd]()
        cmd = input('Please input commmand')
        cmdLowcase =  cmd.lower().strip()
   
def main():
    init()
    run()
​
def test():
    init()
    command['i']()
​
if __name__ == '__main__':
    main()