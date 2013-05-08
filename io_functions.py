# This file is for all functions related to IO

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

def loadTodoList(path):
    #Defines the file to look for
    yourfile = file(listName + ".ser", "r")

    #Loads the targetted file
    currentTodoList = pickle.load(path)  
    print "You've loaded the TodoList " + path
    return currentTodoList




