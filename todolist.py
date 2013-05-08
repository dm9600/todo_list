class TodoList:
    todolist = "empty"
    listName = "no name"

    def __init__(self, todolist, listName):
        self.todolist = todolist
        self.listName = listName

    def addTodo(self, todo):
        if self.todolist == "empty":
            self.todolist = [todo]
        elif isinstance(self.todolist, list):            
            self.todolist.append(todo)

    def sortTodos(self):
        self.todolist = sorted(self.todolist, key=lambda todo: todo.priority)

