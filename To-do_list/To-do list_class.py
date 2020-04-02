import os.path 


class Todolist:
    

    def __init__(self,DataFilename):
        self.DataFilename = DataFilename
        self.TitleList = {}
        self.command = {}
        self.load_toDo()
        self.instruction()
        
    
    def instruction(self):
        
        self.command['a'] = self.createTodo
        self.command['A'] = self.createTodo
        self.command['e'] = self.updateTodo
        self.command['edit'] = self.updateTodo
        self.command['r'] = self.deleteTodo
        self.command['R'] = self.deleteTodo
        self.command['s'] = self.searchTodo
        self.command['search'] = self.searchTodo
        self.command['s'] = self.printTodo
        self.command['S'] = self.printTodo

    def createTodo(self):
        
        title0 = input('input the task title : ')
        if title0 in self.TitleList:
            print ('duplicate task title , Wanna overwrite it ?')
            InputDicsion = input ('y or n : ')
            if InputDicsion == ('y') :
                Todo = input('input the Task : ')
                self.TitleList[title0] = Todo
        
        else :
            Todo = input('input the Task : ')
            self.TitleList[title0] = Todo

    def updateTodo(self):
        pass
        

    def deleteTodo(self):
        
        Todo0 = input('input the task title : ')
        if Todo0 in self.TitleList :
            del self.TitleList[Todo0]
        else :
            print ('not found')

    def searchTodo(self):
        pass

    def printTodo(self):
        
        print(self.TitleList)

    def run(self):
        cmd = input ('Add new task (a/A) or Remove task(r/R) or Show Task(s/S) or quit(q) :')
        cmdLowcase = cmd.lower().strip()

        for i in range (0,10):
            if (cmdLowcase == 'q') or (cmdLowcase =='quit'):
                break
            if cmdLowcase in self.command.keys():
                self.command[cmdLowcase]()
            cmd = input ('Add new task (a/A) or Remove task(r/R) or Show Task(s/S) or quit(q) :')
            cmdLowcase = cmd.lower().strip()

    def save_toDo(self):
       
        file=open(self.DataFilename,"wt")

        for key in self.TitleList.keys():
            file.write(key + '\n'+ self.TitleList[key]+'\n')

        file.close()

    def load_toDo(self):
        
        if os.path.isfile(self.DataFilename) == False:
            return
            

        file=open(self.DataFilename,"rt")
        lines = file.readlines()
        i=0  

        for j in range(10):
            TitleNew = lines[i]
            TitleNew = TitleNew[:-1]
            toDoNew = lines[i+1] 
            toDoNew = toDoNew[:-1]
            self.TitleList[TitleNew] = toDoNew
            i=i+2
            if i >= len(lines):
                break
        print (self.TitleList)

    #def main(self):
        #self.load_toDo()
        #self.instruction()
        #self.run()
        #self.save_toDo()



if __name__ == '__main__':
    todo1=Todolist("e:/todo_list.txt")
    todo1.run()
    todo1.save_toDo()

    todo2=Todolist("e:/todo_list2.txt")
    todo2.run()
    todo2.save_toDo()
    

    #todo2=Todolist("e:/todo_list2.txt")


    
    #test()