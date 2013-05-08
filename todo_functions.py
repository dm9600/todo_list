#This file is for all functions that manipulate todo_list and todo

import pickle
import todo
import todolist

def newTodoList():
    #The initial menu
    print "Hello User, would you like to create a new Todo" \
            "List or modify an existing one?"
    print "a) Create new List"
    print "b) View existing list"
    print "c) Load list from file"
    print "d) Exit"
    response = raw_input(">")

    #If the user decides to create a new list
    if response == "a":
        print "Please give your new list a name"
        listName = raw_input(">")
        newList = TodoList("empty", listName)
        print "You have created a new list with name " + listName 
        viewTodoList(newList)

    elif response == "b":
        #If the user decides to see an existing list
        print "Please enter in your list's name"
        listName = raw_input(">")
        currentTodoList = loadTodoList(listName)
        viewTodoList(currentTodoList)

    elif response == "c":
        #If the user wants to laod from file
        print "Please enter in the name of the file"
        filename = raw_input(">")
        viewTodoList(loadFromFile(filename))
    elif response == "d":
        exit()       

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
    if not isinstance(TodoList.todolist, basestring) and len(TodoList.todolist) > 0:
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


