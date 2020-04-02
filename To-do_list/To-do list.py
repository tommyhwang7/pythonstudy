TitleList = {}
command = {}

def instruction():
    global command
    command['a'] = createTodo
    command['A'] = createTodo
    command['e'] = updateTodo
    command['edit'] = updateTodo
    command['r'] = deleteTodo
    command['R'] = deleteTodo
    command['s'] = searchTodo
    command['search'] = searchTodo
    command['s'] = printTodo
    command['S'] = printTodo

def createTodo():
    global TitleList
    title0 = input('input the task title : ')
    if title0 in TitleList:
        print ('duplicate task title , Wanna overwrite it ?')
        InputDicsion = input ('y or n : ')
        if InputDicsion == ('y') :
            Todo = input('input the Task : ')
            TitleList[title0] = Todo
        
    else :
        Todo = input('input the Task : ')
        TitleList[title0] = Todo

def updateTodo():
    global TitleList

def deleteTodo():
    global TitleList
    Todo0 = input('input the task title : ')
    if Todo0 in TitleList :
        del TitleList[Todo0]
    else :
        print ('not found')

def searchTodo():
    global TitleList

def printTodo():
    global TitleList
    print(TitleList)

def run():
    cmd = input ('Add new task (a/A) or Remove task(r/R) or Show Task(s/S) or quit(q) :')
    cmdLowcase = cmd.lower().strip()

    for i in range (0,10):
        if (cmdLowcase == 'q') or (cmdLowcase =='quit'):
            break
        if cmdLowcase in command.keys():
            command[cmdLowcase]()
        cmd = input ('Add new task (a/A) or Remove task(r/R) or Show Task(s/S) or quit(q) :')
        cmdLowcase = cmd.lower().strip()

def save_toDo():
    global TitleList

    file=open("e:/todo_list.txt","wt")

    for key in TitleList.keys():
        file.write(key + '\n'+ TitleList[key]+'\n')

    file.close()

def load_toDo():
    global TitleList

    file=open("e:/todo_list.txt","rt")
    lines = file.readlines()
    i=0  

    for j in range(10):
        TitleNew = lines[i]
        TitleNew = TitleNew[:-1]
        toDoNew = lines[i+1] 
        toDoNew = toDoNew[:-1]
        TitleList[TitleNew] = toDoNew
        i=i+2
        if i >= len(lines):
            break
    print (TitleList)

def main():
    load_toDo()
    instruction()
    run()
    save_toDo()


if __name__ == '__main__':
    main()
    #test()