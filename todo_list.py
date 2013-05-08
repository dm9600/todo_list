#TodoList version 1.0
#by dm9600
#A simple todo list program

import pickle

def newTodoList():
    #The initial menu
    print "Hello User, would you like to create a new Todo" \
        "List or modify an existing one?"
    print "a) Create new List"
    print "b) View existing list"
    print "c) Load list from file"
    response = raw_input(">")

    #If the user decides to create a new list
    if response == "a":
        print "Please give your new list a name"
        listName = raw_input(">")
        newList = TodoList("empty", listName)
        print "You have created a new list with name " + listName 
        viewTodoList(newList)

    #If the user decides to see an existing list
    elif response == "b":
        print "Please enter in your list's name"
        listName = raw_input(">")
        currentTodoList = loadTodoList(listName)
        viewTodoList(currentTodoList)

    #If the user wants to laod from file
    elif response == "c":
        print "Please enter in the name of the file"
        filename = raw_input(">")
        viewTodoList(loadFromFile(filename))

def addTodo(todoList):
    #Todo item
    print "Please enter something you need to do"    
    newTodoItem = raw_input(">")

    #Todo priority
    print "Now enter in a priority for your todo"
    newPriority = raw_input(">")
    print newPriority

    #Raw input comes out as a string, so it needs to get cast first
    if int(newPriority) > 0 and int(newPriority) <= 10:
        newTodo = Todo(newPriority, newTodoItem)
        todoList.addTodo(newTodo)        
        print "You've created a new Todo: " \
        + newTodoItem + " with a priority of " \
        + newPriority + ". What would you like to do now?"
        print "a) View my list"
        print "b) Save and quit"
        response = raw_input(">")

        #Based on the user response, call the appropriate functions
        if response == "a":
            viewTodoList(todoList)
        elif response == "b":
            saveTodoList(todoList)
            exit()
    else:
        print "Priority needs to be between 0 and 10"
        addTodo(todoList)
    return

#View a todolist, and give lots of options
def viewTodoList(TodoList):
    if not isinstance(TodoList.todolist, basestring) \
            and len(TodoList.todolist) > 0:
        print "Here are the current todos on the list: "
        for todo in TodoList.todolist:
            print todo.getPriority() + ": " + todo.getTodo()

    print "What would you like to do?"
    print "a) Add a todo"
    print "b) Remove a todo"
    print "c) Sort list descending"
    print "d) Save list"
    print "e) Modify Todo"
    print "f) Exit"
    print "g) Save to file"
    
    response = raw_input(">")
    if response == "a":
        addTodo(TodoList)
    elif response == "b":
        print "Please enter the index of the todo to remove"
        index = int(raw_input(">"))
        removeTodo(TodoList, index)
    elif response == "c":
        TodoList.sortTodos()
        print "TodoList has been sorted"
        viewTodoList(TodoList)
    elif response == "d":
        saveTodoList(TodoList)
    elif response == "e":
        print "Please enter in the index of the todo you'd like to modify"
        response = raw_input(">")
        modifyTodo(TodoList, response)
    elif response == "f":
        exitProgram()
    elif response == "g":
        outputAsFile(TodoList, TodoList.listName)
        viewTodoList(TodoList)
    return

#Removes a todo based on a TodoList and the index of the todo on the list
def removeTodo(TodoList, index):
    #Removes the todo from the list and returns removedTodo
    removedTodo = TodoList.todolist.pop(0)
    print "You've removed the following todo from your todolist: " \
        + removedTodo.getTodo()
    print "with priority: " + removedTodo.getPriority()
    #Return to view flow when finished
    viewTodoList(TodoList)
    return

#Modifies the todo at the specified index
def modifyTodo(TodoList, index):
    #Raw input is automatically a string, so convert it to int
    currentTodo = TodoList.todolist[int(index)]
    print "You've selected the todo " + currentTodo.todo
    print "What would you like to do with this todo?"
    print "a) Change it's content"
    print "b) Change it's priority"
    print "c) Delete it"
    print "d) Cancel"
    response = raw_input(">")
    if response == "a":
        changeTodoContent(currentTodo)
        viewTodoList(TodoList)
    elif response == "b":
        changeTodoPriority(currentTodo)
        viewTodoList(TodoList)
    elif response == "c":
        removeTodo(TodoList, index)
    elif response == "d":
        viewTodoList(TodoList)
    return

#Change the "todo" attribute of the Todo class
def changeTodoContent(Todo):
    print "What would you like to change the content to?"
    response = raw_input(">")
    Todo.setTodo(response)
    print "You've changed this todo's content to " + response    
    return

#Change the "priority" attribute of the Todo class
def changeTodoPriority(Todo):
    print "What would you like to change the priority to?"
    response = raw_input(">")
    Todo.setPriority(response)
    return

#Load a todolist from a file. File should be formatted like this:
#"4: Something to do, 3: Something else to do," etc
def loadFromFile(filename):
    #Sets the default return value
    returnValue = TodoList([], "nothing")

    #Reads the file and splits it by commas
    todoStringList = open(filename, "r").read().split(",")

    #Populates the todolist with todos
    todolist = []
    for string in todoStringList:
        todoString = string.strip().split(":")
        todolist.append(Todo(todoString[0], todoString[1]))
        
    #The new list will be named with the filename minus the extension
    filenameNoExt = filename.split(".")
    returnValue = TodoList(todolist, filenameNoExt)    

    return returnValue
    
    #Populate a new todolist with the file contents
    newTodoList = []
    for rawTodo in trimmedFile:
        rawTodoSplit = rawTodo.split(":")
        newTodoList.append(Todo(rawTodoSplit[0], rawTodoSplit[1]))
    
    #Create new list with name filename minus .txt with newTodoList
    returnValue = TodoList(newTodoList, filename.strip(".txt"))
    return returnValue

def outputAsFile(TodoList, filename):
    returnValue = open(filename + ".txt", "w")
    outString = ""
    for index, todo in enumerate(TodoList.todolist):
        outString += todo.priority + ":" + todo.todo
        if not index == len(TodoList.todolist) - 1:
            outString += ","
    returnValue.write(outString)
    print "You've written your todo to the file " \
        + filename + ".txt"
    return 

def exitProgram():
    print "Goodbye User"

def saveTodoList(TodoList):    
    #Creates the filename for the TodoList
    filename = TodoList.listName + ".ser"

    #Defines the file that'll be written. "w" indicates it's writeable
    yourfile = file("output/" + filename, "w")
    
    #Serialize the file
    pickle.dump(TodoList, yourfile)
    print "You've saved your list to " + filename
    
    viewTodoList(TodoList)
    return

def loadTodoList(listName):
    #Defines the file to look for
    yourfile = file(listName + ".ser", "r")
    
    #Loads the targetted file
    currentTodoList = pickle.load(yourfile)  
    print "You've loaded the TodoList " + listName
    return currentTodoList

class TodoList:
    todolist = "empty"
    listName = "no name"
    
    #Constructor
    def __init__(self, todolist, listName):
        self.todolist = todolist
        self.listName = listName

    #Method for adding todos
    def addTodo(self, todo):
        if self.todolist == "empty":
            self.todolist = [todo]
        elif isinstance(self.todolist, list):            
            self.todolist.append(todo)
    
    #Sorting the list by priority
    def sortTodos(self):
        self.todolist = sorted(self.todolist, key=lambda todo: todo.priority)

class Todo:
    priority = 0
    todo = "nothing"

    def __init__(self, priority, todo):
        self.priority = priority
        self.todo = todo

    def setPriority(self, priority):
        self.priority = priority
        
    def getPriority(self):
        return self.priority

    def setTodo(self, todo):
        self.todo = todo
        
    def getTodo(self):
        return self.todo
        

